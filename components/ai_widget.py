"""
ai_widget.py — VNWander floating AI chat widget.
Save this file to: components/ai_widget.py
"""
import streamlit as st
from config.ai_config import init_chat_session, get_history, stream_response


def render_chat_widget() -> None:
    """
    Render the floating chat bubble (bottom-right) + popover panel.
    Call once per page, after all other page content.
    """
    init_chat_session()

    # ── CSS ────────────────────────────────────────────────────────────────────
    # CRITICAL: every line must start at column 0.
    # Streamlit treats any line with 4+ leading spaces as a <pre> code block
    # and renders it as raw text instead of HTML.
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap');

/* ═══════════════════════════════════════════════════
   1. FLOATING BUBBLE — bottom-right, blue circle
═══════════════════════════════════════════════════ */
div[data-testid="stPopover"] {
position: fixed !important;
bottom: 30px !important;
right: 30px !important;
left: auto !important;
top: auto !important;
z-index: 9999 !important;
width: fit-content !important;  /* Prevents Streamlit stretching the wrapper
                                    full-width and creating a wide bar */
}

div[data-testid="stPopover"] > button {
width: 65px !important;
height: 65px !important;
min-width: 65px !important;
min-height: 65px !important;
max-width: 65px !important;
max-height: 65px !important;
border-radius: 50% !important;
background-color: #0056A3 !important;
color: #ffffff !important;
border: 3px solid #ffffff !important;
box-shadow: 0 6px 24px rgba(0,86,163,0.45) !important;
padding: 0 !important;
font-size: 1.6rem !important;
line-height: 1 !important;
display: flex !important;
align-items: center !important;
justify-content: center !important;
overflow: hidden !important;
transition: transform 0.22s ease, box-shadow 0.22s ease !important;
}
div[data-testid="stPopover"] > button:hover {
transform: scale(1.1) !important;
box-shadow: 0 12px 32px rgba(0,86,163,0.55) !important;
}

/* ═══════════════════════════════════════════════════
   2. CHAT WINDOW — 450px wide, white bg, blue border
═══════════════════════════════════════════════════ */
div[data-testid="stPopoverBody"] {
width: 450px !important;
min-width: 450px !important;
background-color: #ffffff !important;
border: 2px solid #0056A3 !important;
border-radius: 16px !important;
box-shadow: 0 16px 48px rgba(0,86,163,0.18) !important;
padding: 0 !important;
overflow: hidden !important;
font-family: 'DM Sans', sans-serif !important;
color: #111111 !important;
}

/* Force white background and black text on ALL children */
div[data-testid="stPopoverBody"] * {
color: #111111 !important;
background-color: transparent !important;
}

/* ═══════════════════════════════════════════════════
   3. HEADER BAR
═══════════════════════════════════════════════════ */
.vnw-header {
background: linear-gradient(135deg, #0056A3, #1a7fd4) !important;
padding: 13px 16px !important;
display: flex !important;
align-items: center !important;
gap: 10px !important;
}
.vnw-header-title {
font-family: 'DM Sans', sans-serif !important;
font-size: 0.95rem !important;
font-weight: 600 !important;
color: #ffffff !important;
letter-spacing: 0.2px !important;
}
.vnw-dot {
width: 9px !important;
height: 9px !important;
border-radius: 50% !important;
background: #5fffaa !important;
box-shadow: 0 0 7px #5fffaa !important;
flex-shrink: 0 !important;
animation: vnwpulse 2s ease-in-out infinite !important;
}
@keyframes vnwpulse {
0%, 100% { opacity: 1; }
50%       { opacity: 0.3; }
}

/* ═══════════════════════════════════════════════════
   4. MESSAGE BUBBLES — white bg, blue border, black text
      User → right-aligned | AI → left-aligned
═══════════════════════════════════════════════════ */

/* Base bubble reset */
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] {
background-color: #ffffff !important;
border: 1.5px solid #0056A3 !important;
border-radius: 14px !important;
padding: 10px 14px !important;
font-size: 0.88rem !important;
font-family: 'DM Sans', sans-serif !important;
max-width: 80% !important;
color: #111111 !important;
}

/* User messages — push to the right */
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
margin-left: auto !important;
margin-right: 0 !important;
flex-direction: row-reverse !important;
background-color: #ffffff !important;
border-color: #0056A3 !important;
}

/* AI messages — stay on the left */
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
margin-left: 0 !important;
margin-right: auto !important;
background-color: #ffffff !important;
border-color: #0056A3 !important;
}

/* All text inside bubbles — black */
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] p,
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] span,
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] div,
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] li {
color: #111111 !important;
background-color: transparent !important;
}

/* ═══════════════════════════════════════════════════
   5. SCROLLABLE MESSAGE AREA
═══════════════════════════════════════════════════ */
div[data-testid="stPopoverBody"] [data-testid="stVerticalBlockBorderWrapper"] {
overflow-y: auto !important;
max-height: 380px !important;
background-color: #ffffff !important;
padding: 10px !important;
}

/* ═══════════════════════════════════════════════════
   6. INPUT FIELD — black text, white bg, blue border
═══════════════════════════════════════════════════ */
div[data-testid="stPopoverBody"] input[type="text"] {
background-color: #ffffff !important;
color: #111111 !important;
caret-color: #111111 !important;
border: 2px solid #0056A3 !important;
border-radius: 10px !important;
font-family: 'DM Sans', sans-serif !important;
font-size: 0.9rem !important;
padding: 8px 12px !important;
}
div[data-testid="stPopoverBody"] input[type="text"]:focus {
border-color: #003f7a !important;
box-shadow: 0 0 0 3px rgba(0,86,163,0.15) !important;
outline: none !important;
}
div[data-testid="stPopoverBody"] input[type="text"]::placeholder {
color: #7a9bbf !important;
}

/* ═══════════════════════════════════════════════════
   7. SEND BUTTON
═══════════════════════════════════════════════════ */
div[data-testid="stPopoverBody"] [data-testid="stFormSubmitButton"] button {
background-color: #0056A3 !important;
color: #ffffff !important;
border: none !important;
border-radius: 10px !important;
font-family: 'DM Sans', sans-serif !important;
font-weight: 600 !important;
font-size: 0.9rem !important;
padding: 0.45rem 1rem !important;
width: 100% !important;
transition: background-color 0.2s ease !important;
}
div[data-testid="stPopoverBody"] [data-testid="stFormSubmitButton"] button:hover {
background-color: #003f7a !important;
}

/* ═══════════════════════════════════════════════════
   8. REMOVE DEFAULT FORM BORDER
═══════════════════════════════════════════════════ */
div[data-testid="stPopoverBody"] [data-testid="stForm"] {
border: none !important;
padding: 10px !important;
background-color: #f5f9ff !important;
border-top: 1px solid #dceeff !important;
}
</style>
""", unsafe_allow_html=True)

    # ── Popover ────────────────────────────────────────────────────────────────
    with st.popover("💬"):   # Icon-only label keeps the button a true circle

        # Header
        st.markdown("""
<div class="vnw-header">
<div class="vnw-dot"></div>
<span class="vnw-header-title">🌿 Chat Box AI VNWander</span>
</div>
""", unsafe_allow_html=True)

        # Error guard
        if st.session_state.get("chat_error"):
            st.error("❌ Không thể kết nối AI.")
            return

        # ── Scrollable message history ─────────────────────────────────────────
        # History is Groq-format dicts: {"role": "user"/"assistant", "content": "..."}
        chat_box = st.container(height=360)
        with chat_box:
            history = get_history()
            if not history:
                with st.chat_message("assistant", avatar="🌿"):
                    st.markdown("Xin chào! Tôi là **Chat Box AI VNWander**. Hello! I'm **Chat Box AI VNWander**. Tôi có thể giúp gì cho chuyến đi của bạn? / How can I help with your trip? 🌏")
            for msg in history:
                role   = msg["role"]
                avatar = "🧑" if role == "user" else "🌿"
                with st.chat_message(role, avatar=avatar):
                    st.markdown(msg["content"])

        # ── Input form ─────────────────────────────────────────────────────────
        # FIX: clear_on_submit=True wipes the widget value to "" before the
        # handler block runs, so checking `user_input` is always False.
        # We save the value into session_state INSIDE the form (while it still
        # exists), then read + pop it OUTSIDE the form after the clear.
        with st.form("vnw_widget_form", clear_on_submit=True):
            cols = st.columns([5, 1])
            with cols[0]:
                typed = st.text_input(
                    "msg",
                    placeholder="Hỏi về du lịch Việt Nam…",
                    label_visibility="collapsed",
                    key="vnw_typed",
                )
            with cols[1]:
                submitted = st.form_submit_button("➤")

            # Capture while the value still exists
            if submitted:
                st.session_state["vnw_pending"] = typed

        # ── Handle submission — safe outside the form ──────────────────────────
        pending = st.session_state.pop("vnw_pending", "")
        if pending:
            with chat_box:
                with st.chat_message("user", avatar="🧑"):
                    st.markdown(pending)
                with st.chat_message("assistant", avatar="🌿"):
                    placeholder = st.empty()
                    full_text = ""
                    for chunk in stream_response(pending):
                        full_text += chunk
                        placeholder.markdown(full_text + "▌")
                    placeholder.markdown(full_text)
            st.rerun()