"""
8_AI_Assistant.py — VNWander full-page AI Travel Guide chat interface.
Uses the shared ai_config module for state, persona, and streaming.
"""
import streamlit as st
from config.ai_config import init_chat_session, get_history, stream_response

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Linh – VNWander AI Guide",
    page_icon="🌿",
    layout="centered",
)

# ── Shared session init ────────────────────────────────────────────────────────
init_chat_session()

# ── Custom CSS ────────────────────────────────────────────────────────────────
# All lines start at column 0 — Streamlit treats 4-space-indented lines as <pre>.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap');

/* Page background */
[data-testid="stAppViewContainer"] {
background: linear-gradient(160deg, #f0f7ff 0%, #fafcff 60%, #f5f0eb 100%);
}

/* Hide default Streamlit chrome */
[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

/* Chat title */
.vnw-title {
font-family: 'Lora', serif;
font-size: 2rem;
font-weight: 600;
color: #0056A3;
letter-spacing: -0.5px;
margin-bottom: 0.1rem;
}
.vnw-subtitle {
font-family: 'DM Sans', sans-serif;
font-size: 0.9rem;
color: #7a9bbf;
margin-bottom: 2rem;
letter-spacing: 0.3px;
}

/* Fixed chat input at bottom */
.fixed-chat-input {
position: fixed;
bottom: 0;
left: 0;
width: 100%;
background: #ffffff;
padding: 12px 20px;
border-top: 1px solid #0056A3;
z-index: 1000;
box-sizing: border-box;
}

/* Single scrollable chat container */
.chat-scroll-container {
height: 65vh;
min-height: 400px;
max-height: 70vh;
overflow-y: auto !important;
padding: 0 8px 80px 8px; /* bottom padding ensures last message not hidden behind fixed input */
background: transparent;
scroll-behavior: smooth;
}

/* Ensure messages don't have their own scroll */
.stChatMessage {
overflow: visible !important;
max-height: none !important;
}

/* Chat container */
[data-testid="stChatMessageContent"],
[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"],
.stChatMessage {
background: #ffffff !important;
}

/* Chat input area wrapper */
[data-testid="stChatInput"] {
background: #ffffff !important;
}

/* Chat message bubbles - all messages */
[data-testid="stChatMessage"] {
font-family: 'DM Sans', sans-serif;
border-radius: 16px;
padding: 0.25rem 0.5rem;
background: #ffffff !important;
border: 1px solid #0056A3 !important;
overflow: visible !important;
}

/* User bubble */
[data-testid="stChatMessage"][data-testid*="user"],
div[class*="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
background: #ffffff !important;
border: 1px solid #0056A3 !important;
}

/* User bubble text */
[data-testid="stChatMessage"][data-testid*="user"] *,
div[class*="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) * {
color: #000000 !important;
}

/* Assistant bubble */
div[class*="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
background: #ffffff !important;
border: 1px solid #0056A3 !important;
}

/* Assistant bubble text */
div[class*="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) * {
color: #000000 !important;
}

/* Chat input */
[data-testid="stChatInput"] textarea {
font-family: 'DM Sans', sans-serif;
border-radius: 14px !important;
border: 2px solid #0056A3 !important;
background: #ffffff !important;
color: #000000 !important;
font-size: 0.95rem;
}
[data-testid="stChatInput"] textarea:focus {
border-color: #0056A3 !important;
box-shadow: 0 0 0 3px rgba(0,86,163,0.10) !important;
}

/* Chat input placeholder */
[data-testid="stChatInput"] textarea::placeholder {
color: #6c757d !important;
}

/* Suggestion chips */
.chip-row {
display: flex;
flex-wrap: wrap;
gap: 8px;
margin: 1rem 0 1.5rem;
}
.chip {
display: inline-block;
background: #ffffff;
border: 1.5px solid #c5dcf5;
border-radius: 50px;
padding: 6px 16px;
font-family: 'DM Sans', sans-serif;
font-size: 0.82rem;
font-weight: 500;
color: #0056A3;
cursor: pointer;
transition: all 0.2s ease;
}
.chip:hover {
background: #0056A3;
color: #ffffff;
border-color: #0056A3;
}

/* Status badge */
.status-badge {
display: inline-flex;
align-items: center;
gap: 6px;
font-family: 'DM Sans', sans-serif;
font-size: 0.78rem;
color: #52a56e;
font-weight: 600;
letter-spacing: 0.3px;
}
.status-dot {
width: 7px; height: 7px;
background: #52a56e;
border-radius: 50%;
animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
0%, 100% { opacity: 1; transform: scale(1); }
50%       { opacity: 0.5; transform: scale(0.85); }
}

/* Thin blue scrollbar matching VNWander theme */
::-webkit-scrollbar {
width: 8px !important;
height: 8px !important;
}
::-webkit-scrollbar-track {
background: transparent !important;
}
::-webkit-scrollbar-thumb {
background: #c5dcf5 !important;
border-radius: 4px !important;
}
::-webkit-scrollbar-thumb:hover {
background: #0056A3 !important;
}
* {
scrollbar-width: thin !important;
scrollbar-color: #c5dcf5 transparent !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<p class="vnw-title">🌿 Linh — VNWander Guide</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="vnw-subtitle">Trợ lý du lịch AI của bạn · Your personal Vietnam travel AI</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<span class="status-badge"><span class="status-dot"></span>Đang hoạt động · Online</span>',
    unsafe_allow_html=True,
)

# ── Error guard ────────────────────────────────────────────────────────────────
if st.session_state.get("chat_error"):
    st.error(f"❌ Không thể kết nối AI: {st.session_state.chat_error}")
    st.stop()

# ── Fixed chat input at bottom (outside scrollable area) ───────────────────────
st.markdown('<div class="fixed-chat-input">', unsafe_allow_html=True)
user_input = st.chat_input("Hỏi Linh về du lịch Việt Nam…")
st.markdown('</div>', unsafe_allow_html=True)

# ── Single scrollable container for ALL chat messages ─────────────────────────
st.markdown('<div class="chat-scroll-container" id="chat-container">', unsafe_allow_html=True)

# ── Suggestion chips (only shown when history is empty) ───────────────────────
SUGGESTIONS = [
    "🏖️ Bãi biển đẹp nhất Việt Nam?",
    "🍜 Ẩm thực Hội An phải thử",
    "🗺️ Lịch trình 7 ngày miền Bắc",
    "🛵 Thuê xe máy ở Hà Nội",
]

if not get_history():
    st.markdown(
        '<div class="chip-row">'
        + "".join(f'<span class="chip">{s}</span>' for s in SUGGESTIONS)
        + "</div>",
        unsafe_allow_html=True,
    )
    # Greeting message
    with st.chat_message("assistant", avatar="🌿"):
        st.markdown(
            "Xin chào! Tôi là **Linh**, hướng dẫn viên AI của VNWander. "
            "Tôi có thể giúp bạn khám phá vẻ đẹp tuyệt vời của Việt Nam — "
            "từ những bãi biển huyền bí đến những con phố cổ kính. "
            "Bạn đang lên kế hoạch cho chuyến đi nào vậy? 🌏"
        )

# ── Render existing history ────────────────────────────────────────────────────
for message in get_history():
    role   = "user" if message["role"] == "user" else "assistant"
    avatar = "🧑" if role == "user" else "🌿"
    with st.chat_message(role, avatar=avatar):
        st.markdown(message["content"])

# ── Handle new user input: render inside the same container ───────────────────
if user_input:
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)
    with st.chat_message("assistant", avatar="🌿"):
        st.write_stream(stream_response(user_input))

# Close the scrollable container
st.markdown('</div>', unsafe_allow_html=True)

# ── Auto-scroll to bottom on each update ───────────────────────────────────────
st.markdown("""
<script>
(function() {
    const container = document.querySelector('.chat-scroll-container');
    if (!container) return;

    // Avoid attaching multiple observers
    if (container.getAttribute('data-scroll-observer-attached')) return;
    container.setAttribute('data-scroll-observer-attached', 'true');

    function scrollToBottom() {
        container.scrollTop = container.scrollHeight;
    }

    // Initial scroll
    scrollToBottom();

    // Watch for new messages being added
    const observer = new MutationObserver(function(mutations) {
        let shouldScroll = false;
        for (let mutation of mutations) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                shouldScroll = true;
                break;
            }
        }
        if (shouldScroll) {
            scrollToBottom();
        }
    });

    observer.observe(container, { childList: true, subtree: true });
})();
</script>
""", unsafe_allow_html=True)