"""
ai_config.py — VNWander AI config using Groq (free, no credit card required).
Get a free API key in 30 seconds at: https://console.groq.com
Save this file to: config/ai_config.py
"""
import streamlit as st
import time
from groq import Groq, RateLimitError, APIError, APIConnectionError, APITimeoutError

# ── Free Groq API key ──────────────────────────────────────────────────────────
# Get yours free at https://console.groq.com → "Create API Key"
# Free tier: 14,400 requests/day · 500,000 tokens/minute · no credit card needed
GROQ_API_KEY = "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"
GROQ_MODEL   = "llama-3.1-8b-instant"   # fast & free; swap to
                                          # "llama-3.3-70b-versatile" for smarter answers

SYSTEM_PROMPT = (
    "You are Chat Box AI VNWander, the official AI Travel Guide for VNWander — "
    "Vietnam's premier travel platform. "
    "LANGUAGE RULE (highest priority): detect the language of every user message "
    "and reply fluently in that exact language. If the user writes in Vietnamese, "
    "respond entirely in Vietnamese. If the user writes in English, respond entirely "
    "in English. Never mix languages in a single reply. "
    "Help travellers discover Vietnam with warmth and expertise. "
    "Be concise but vivid. Use bullet points for lists, prose for recommendations. "
    "Cover all 63 provinces: history, culture, cuisine, hidden gems, transport, "
    "seasons, etiquette, safety, and budget guidance. "
    "Never invent prices — say 'check vnwander.com for current rates.' "
    "If asked something off-topic, gently redirect to Vietnam travel. "
    "End your first reply with a follow-up question to personalise advice. "
    "Always introduce yourself as 'Chat Box AI VNWander' when asked who you are."
)


def init_chat_session() -> None:
    """
    Initialise the Groq client and an empty message history in session_state.
    History is stored as a plain list of {"role": ..., "content": ...} dicts
    (OpenAI-compatible format) so it works directly with the Groq SDK.
    Safe to call on every page load — only runs once per browser session.
    """
    if "groq_client" not in st.session_state:
        try:
            st.session_state.groq_client  = Groq(api_key=GROQ_API_KEY)
            st.session_state.chat_history  = []   # list of {"role", "content"} dicts
            st.session_state.chat_error    = None
        except Exception as exc:
            st.session_state.groq_client  = None
            st.session_state.chat_history  = []
            st.session_state.chat_error    = str(exc)


def get_history() -> list:
    """Return the current chat history as a list of dicts, or [] on failure."""
    return st.session_state.get("chat_history", [])


def stream_response(user_input: str):
    """
    Append the user message to history, call Groq with streaming,
    yield each text chunk, then append the completed assistant reply to history.
    Use with a manual chunk loop (works inside both st.write_stream and popovers).
    """
    client = st.session_state.get("groq_client")
    if client is None:
        yield "⚠️ AI chưa được khởi tạo. Vui lòng tải lại trang."
        return

    # Add user turn to history
    history: list = st.session_state.chat_history
    history.append({"role": "user", "content": user_input})

    try:
        stream = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            stream=True,
            temperature=0.7,
            max_tokens=1024,
        )

        full_reply = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            if delta:
                full_reply += delta
                yield delta

        # Persist completed assistant reply
        history.append({"role": "assistant", "content": full_reply})

    except RateLimitError:
        time.sleep(1)
        error_msg = "⚠️ Ai đó đang hỏi Linh quá nhanh — vui lòng thử lại sau vài giây."
        history.pop()
        yield error_msg
    except APITimeoutError:
        error_msg = "⚠️ Mất kết nối đến AI. Vui lòng thử lại."
        history.pop()
        yield error_msg
    except APIError as exc:
        error_msg = f"⚠️ Lỗi từ AI ({getattr(exc, 'status_code', '?')}): {exc}"
        history.pop()
        yield error_msg
    except Exception as exc:
        error_msg = f"⚠️ Lỗi không xác định: {exc}"
        history.pop()
        yield error_msg