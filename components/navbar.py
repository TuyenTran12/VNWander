import streamlit as st
from config.languages import CONTENT

def render_navbar(current_page_path="/"):
    """
    Renders navbar và giữ lại trang hiện tại khi chuyển ngôn ngữ.
    current_page_path: "/" cho trang chủ, "/Team" cho trang đội ngũ.
    """
    # 1. Lấy ngôn ngữ hiện tại
    lang = st.session_state.get('lang', 'vi')
    L = CONTENT[lang]

    # 2. Xác định ngôn ngữ tiếp theo để hiển thị trên nút bấm
    next_lang = 'en' if lang == 'vi' else 'vi'
    lang_label = 'EN' if lang == 'vi' else 'VI'

    # 3. Tạo HTML Navbar
    st.markdown(f"""
    <div class="vn-navbar">
        <div class="vn-navbar-inner">
            <div class="vn-nav-left">
                <a href="/?lang={lang}" class="vn-logo" target="_self">VNWander</a>
                <a href="{current_page_path}?lang={next_lang}" target="_self" class="vn-lang-btn">{lang_label}</a>
            </div>
            <div class="vn-nav-right">
                <a href="/?lang={lang}" class="vn-nav-link" target="_self">{L['navbar']['home']}</a>
                <a href="/Team?lang={lang}" class="vn-nav-link" target="_self">{L['navbar']['team']}</a>
                <a href="/Careers?lang={lang}" class="vn-nav-link" target="_self">{L['navbar']['career']}</a>
                <a href="/News?lang={lang}" class="vn-nav-link" target="_self">{L['navbar']['news']}</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)