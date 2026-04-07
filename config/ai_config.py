"""
config/ai_config.py — Shared AI configuration for VNWander.
Provides session init, history, streaming, and DB persistence.
Uses Google Gemini API via the modern google-genai SDK.
"""
import streamlit as st
from google import genai
from google.genai import types
from dataclasses import dataclass
from typing import Iterator, List

from core.db_engine import init_connection


# ── Constants ──────────────────────────────────────────────────────────────────
def get_gemini_api_key() -> str:
    """Fetch API key from st.secrets or streamlit config."""
    secret = st.secrets.get("GEMINI_API_KEY", "")
    return secret


# Targeting google-genai v1.x; model: gemini-1.5-flash (valid, low-latency)
MODEL = "gemini-1.5-flash"

SYSTEM_PROMPT = (
    "Bạn là một trợ lý du lịch AI của VNWander — nền tảng khám phá du lịch Việt Nam. "
    "Bạn thân thiện, am hiểu về văn hóa, ẩm thực, địa điểm du lịch, lịch trình, "
    "giao thông, và các trải nghiệm tại Việt Nam. "
    "Trả lời gọn gàng, có cấu trúc, luôn bằng tiếng Việt trừ khi người dùng hỏi tiếng khác. "
    "Hãy gợi ý cụ thể, có thể đề xuất nhà hàng, khách sạn, hoạt động. "
    "Không bịa thông tin — nếu không chắc, hãy nói rõ."
)


# ── Gemini models ──────────────────────────────────────────────────────────────
@dataclass
class ChatMessage:
    role: str  # "user" or "assistant"
    parts: list  # list of part objects with .text attribute


class TextPart:
    __slots__ = ("text",)

    def __init__(self, text: str):
        self.text = text


def _make_msg(role: str, text: str) -> ChatMessage:
    return ChatMessage(role=role, parts=[TextPart(text=text)])


# ── Database persistence ───────────────────────────────────────────────────────
def _create_table_if_missing() -> None:
    """Ensure ai_chat_history table exists in SQL Server."""
    conn = init_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ai_chat_history' AND xtype='U')
            CREATE TABLE ai_chat_history (
                id INT IDENTITY(1,1) PRIMARY KEY,
                [role] NVARCHAR(20) NOT NULL,
                [content] NVARCHAR(MAX) NOT NULL,
                created_at DATETIME2 DEFAULT SYSDATETIME()
            )
        """)
        conn.commit()
    except Exception:
        conn.rollback()
    finally:
        cursor.close()


def save_message_to_db(role: str, content: str) -> None:
    """Persist a single chat message to DB."""
    conn = init_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO ai_chat_history ([role], [content]) VALUES (?, ?)",
            (role, content),
        )
        conn.commit()
    except Exception as e:
        st.warning(f"Không thể lưu tin nhắn: {e}")
    finally:
        cursor.close()


def load_history_from_db() -> List[ChatMessage]:
    """Load entire chat history from DB."""
    conn = init_connection()
    if conn is None:
        return []
    cursor = conn.cursor()
    messages = []
    try:
        cursor.execute("SELECT [role], [content] FROM ai_chat_history ORDER BY id")
        for role, content in cursor.fetchall():
            messages.append(_make_msg(role, content))
    except Exception:
        pass
    finally:
        cursor.close()
    return messages


# ── Client ─────────────────────────────────────────────────────────────────────
_client = None


def _get_client():
    """Get or create the genai.Client singleton."""
    global _client
    if _client is None:
        api_key = get_gemini_api_key()
        if not api_key:
            raise ValueError(
                "Thiếu API key — vui lòng kiểm tra .streamlit/secrets.toml"
            )
        _client = genai.Client(api_key=api_key)
    return _client


# ── Session state helpers ──────────────────────────────────────────────────────
def init_chat_session() -> None:
    """Initialize chat session (idempotent)."""
    _create_table_if_missing()
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = load_history_from_db()
    # Do NOT set a default chat_error key — only exists when an actual error occurs


def get_history() -> List[ChatMessage]:
    """Return current session history."""
    return st.session_state.get("chat_session", [])


def _persist_messages(messages: List[ChatMessage]) -> None:
    """Replace DB history with current session state (simple sync strategy)."""
    conn = init_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM ai_chat_history")
        for msg in messages:
            content = msg.parts[0].text if msg.parts else ""
            cursor.execute(
                "INSERT INTO ai_chat_history ([role], [content]) VALUES (?, ?)",
                (msg.role, content),
            )
        conn.commit()
    except Exception as e:
        st.warning(f"Không thể đồng bộ lịch sử: {e}")
        conn.rollback()
    finally:
        cursor.close()


# ── Streaming API ──────────────────────────────────────────────────────────────
def stream_response(user_input: str) -> Iterator[str]:
    """
    Send user message to Gemini, stream response tokens.
    Uses the modern google-genai SDK (genai.Client.generate_content_stream).
    Appends user + assistant messages to session state and persists to DB.
    """
    api_key = get_gemini_api_key()
    if not api_key:
        st.session_state.chat_error = "Thiếu API key — vui lòng kiểm tra .streamlit/secrets.toml"
        return

    client = _get_client()

    # Build conversation history from session state
    current_session = st.session_state.chat_session

    history_contents = []
    session_history = get_history()
    for msg in session_history:
        role = "model" if msg.role == "assistant" else msg.role
        content = msg.parts[0].text if msg.parts else ""
        history_contents.append(
            types.Content(
                role=role,
                parts=[types.Part(text=content)],
            )
        )

    # Add user message to session immediately
    current_session.append(_make_msg("user", user_input))

    # Configure generation with system instruction
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
    )

    full_response = ""
    try:
        response = client.models.generate_content_stream(
            model=MODEL,
            contents=history_contents + [
                types.Content(
                    role="user",
                    parts=[types.Part(text=user_input)],
                )
            ],
            config=config,
        )
        for chunk in response:
            if chunk.text:
                full_response += chunk.text
                yield chunk.text

    except Exception as e:
        error_msg = str(e)
        st.session_state.chat_error = error_msg
        yield f"Error: {error_msg}"
        return

    # Success — clear any previous error
    st.session_state.pop("chat_error", None)

    # Persist assistant response
    current_session.append(_make_msg("assistant", full_response))
    _persist_messages(current_session)
