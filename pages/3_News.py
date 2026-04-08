import streamlit as st
import textwrap
from components.ai_widget import render_chat_widget
from components.navbar import render_navbar
from components.footer import render_footer
from utils.helpers import load_all_global_css
from utils.session_init import init_session_state
from config.languages import CONTENT

def main():
    # 1. Khởi tạo trang
    st.set_page_config(page_title="VNWander - News", layout="wide")
    init_session_state()
    load_all_global_css()

    if "lang" in st.query_params:
        st.session_state.lang = st.query_params["lang"]
    elif 'lang' not in st.session_state:
        st.session_state.lang = 'vi'

    # 2. Điều hướng
    render_navbar(current_page_path="/News")

    # Hàm hỗ trợ render HTML sạch sẽ
    def render_clean_html(html_code):
        st.markdown(textwrap.dedent(html_code), unsafe_allow_html=True)

    # 3. Lấy dữ liệu
    lang = st.session_state.get('lang', 'vi')
    N = CONTENT[lang]['news_page']

    # Gom bài viết vào 1 danh sách
    articles = []
    if 'featured_post' in N: articles.append(N['featured_post'])
    if 'latest_news' in N: articles.extend(N['latest_news'])

    # 4. TIÊU ĐỀ TRANG (Cũng căn giữa 50%)
    render_clean_html(f"""
        <div style="width: 50%; margin: 0 auto 60px auto; text-align: left;">
            <h1 style="font-family: 'Playfair Display', serif; font-size: 3rem; color: #111; margin: 0;">
                {N.get('title_latest', 'Bản Tin')}
            </h1>
            <div style="width: 50px; height: 5px; background: #4CB5F9; margin-top: 15px;"></div>
        </div>
    """)

    # 5. VÒNG LẶP: CARD 50% - ẢNH TRÊN - CHỮ DƯỚI
    for art in articles:
        render_clean_html(f"""
            <div class="vn-news-card-50">
                <img src="{art.get('img', '')}" alt="news-image">
                <div class="vn-news-info-box">
                    <span style="color: #4CB5F9; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 0.75rem; display: block; margin-bottom: 10px;">
                        {art.get('tag', 'TIN TỨC')}
                    </span>
                    <h2 class="vn-news-title-modern">{art.get('title', '')}</h2>
                    <p class="vn-news-summary-modern">{art.get('summary', '')}</p>
                    <div class="vn-news-footer-modern">
                        <span>{art.get('author', 'VNWander')} • {art.get('date', '')}</span>
                        <a href="#" style="color: #0056A3; font-weight: 700; text-decoration: none;">Đọc thêm →</a>
                    </div>
                </div>
            </div>
        """)

    # 6. Render Footer
    render_footer()
    render_chat_widget()

if __name__ == "__main__":
    main()