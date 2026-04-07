"""
ai_widget.py — VNWander floating AI chat widget.
Drop render_chat_widget() at the bottom of any Streamlit page.
Uses the shared ai_config module — chat history is synced with 8_AI_Assistant.py.

Design: pure white background, solid blue (#0056A3) border, black (#000000) text,
circular button at bottom-left.
"""
import streamlit as st
from config.ai_config import init_chat_session, get_history, stream_response


def render_chat_widget() -> None:
    """
    Render the floating button + popover panel.
    Call once per page, after all other page content.
    """
    init_chat_session()

    # ── Widget CSS ──
    st.markdown("""
<style>
/* ── Floating circular button at bottom-left ── */
.vnw-chat-btn {
    position: fixed !important;
    bottom: 24px !important;
    left: 24px !important;
    width: 56px !important;
    height: 56px !important;
    border-radius: 50% !important;
    background: #FFFFFF !important;
    border: 2px solid #0056A3 !important;
    color: #000000 !important;
    font-size: 24px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    z-index: 9999 !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.2) !important;
}
.vnw-chat-btn:hover {
    background: #0056A3 !important;
    color: #FFFFFF !important;
}

/* ── Popover container — pure white, blue border ── */
div[data-testid="stPopover"] {
    background: #FFFFFF !important;
    border: 2px solid #0056A3 !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 20px rgba(0, 86, 163, 0.15) !important;
    padding: 16px !important;
}

div[data-testid="stPopover"] > div {
    background: #FFFFFF !important;
}

/* ── All text in widget — black ── */
div[data-testid="stPopover"] * {
    color: #000000 !important;
}

/* ── Chat message boxes ── */
div[data-testid="stChatMessage"],
.stChatMessage {
    background: #FFFFFF !important;
    border: 1px solid #0056A3 !important;
}

.stChatMessage * {
    color: #000000 !important;
}

/* ── Input field ── */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    color: #000000 !important;
    background: #FFFFFF !important;
    border: 1px solid #0056A3 !important;
}

/* ── Button / send icon ── */
.stFormItem button,
div[data-testid="stPopover"] .stButton button {
    background: #0056A3 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 50% !important;
    width: 40px !important;
    height: 40px !important;
    min-height: 40px !important;
    padding: 8px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.stFormItem button:hover,
div[data-testid="stPopover"] .stButton button:hover {
    background: #004080 !important;
}

/* ── Warning/error messages ── */
div[data-testid="stPopover"] .stAlert {
    border-color: #0056A3 !important;
    background: #FFFFFF !important;
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

    # ── Panel header ──────────────────────────────────────────────────
    with st.popover("💬"):
        st.markdown(
            """
<div class="vn-widget-header">
    <span class="vn-widget-dot"></span>
    <span class="vn-widget-header-title">Linh — VNWander Guide</span>
</div>
""",
            unsafe_allow_html=True,
        )

        # ── Error display (non-blocking) ──────────────────────────────────
        err = st.session_state.get("chat_error")
        if err:
            st.warning(f"{err}")

        # ── Scrollable message history ────────────────────────────────────
        chat_box = st.container(height=340)
        with chat_box:
            history = get_history()
            if not history:
                with st.chat_message("assistant", avatar="🌿"):
                    st.markdown("Xin chào! Tôi là Linh, trợ lý AI cho du lịch Việt Nam.")
            for msg in history:
                role = "user" if msg.role == "user" else "assistant"
                avatar = "🧑" if role == "user" else "🌿"
                with st.chat_message(role, avatar=avatar):
                    st.markdown(msg.parts[0].text)

        # ── Input form ────────────────────────────────────────────────────
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

            # Save value NOW, before clear_on_submit destroys it
            if submitted:
                st.session_state["vnw_pending"] = typed

        # ── Handle outside the form — value is safe in session_state ──────
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


if __name__ == "__main__":
    render_chat_widget()
