import streamlit as st
import os
import datetime
from utils.helpers import get_local_img_url
from components.navbar import render_navbar
from components.search_bar import render_search_bar
from components.hero import render_hero
from components.footer import render_footer
from config.languages import CONTENT

# ------------------------------------------------------------------------------
# Helper: Lấy danh sách thành phố
# ------------------------------------------------------------------------------
def get_all_cities(destinations_data):
    cities = set()
    for region in destinations_data.get('regions', {}).values():
        for city in region.get('cities', []):
            cities.add(city['name'])
    return sorted(list(cities))

# ------------------------------------------------------------------------------
# MAIN APP
# ------------------------------------------------------------------------------
def main():
    st.set_page_config(page_title="VNWander - Khám Phá Việt Nam", layout="wide", initial_sidebar_state="collapsed")
    
    # Load CSS (Giữ nguyên logic của bạn)
    css_files = ["assets/css/base.css", "assets/css/navbar.css", "assets/css/hero.css", "assets/css/components.css", "assets/css/footer.css", "assets/css/style.css"]
    combined_css = ""
    for css_file in css_files:
        if os.path.exists(css_file):
            with open(css_file, encoding="utf-8") as f:
                combined_css += f.read() + "\n\n"
    if combined_css:
        st.markdown(f"<style>{combined_css}</style>", unsafe_allow_html=True)

    # Khởi tạo session state
    if 'lang' not in st.session_state:
        st.session_state.lang = 'vi'
    lang = st.session_state.lang
    
    # ── NAVBAR & HERO & SEARCH BAR ─────────────────────────────────────────────
    render_navbar(current_page_path="/")
    render_hero()
    
    # Bao bọc Search bar trong container để CSS đẩy nó lên trên Hero
    st.markdown('<div class="premium-search-wrapper">', unsafe_allow_html=True)
    render_search_bar()
    st.markdown('</div>', unsafe_allow_html=True)

    # ── DỮ LIỆU TỪ NGÔN NGỮ ────────────────────────────────────────────────────
    D = CONTENT[lang].get('destinations', {})
    A = CONTENT[lang].get('about', {})
    R = CONTENT[lang].get('reviews', {})
# ==============================================================================
    # SECTION 1: ĐIỂM ĐẾN YÊU THÍCH
    # ==============================================================================
    st.markdown(
        '<div class="section-heading-container">'
        '<span class="feature-label">KHÁM PHÁ VIỆT NAM</span>'
        f'<h2 class="section-heading">{D.get("title", "Điểm đến yêu thích")}</h2>'
        '</div>', 
        unsafe_allow_html=True
    )

    regions = D.get('regions', {})
    if regions:
        region_keys = list(regions.keys())
        
        # SỬA LỖI 1: Lấy tên vùng miền từ key 'label' (ví dụ: "North Vietnam")
        region_names = [regions[k].get('label', k) for k in region_keys]
        
        # Tabs chuyển vùng miền
        selected_region_name = st.radio("Chọn vùng miền", region_names, horizontal=True, label_visibility="collapsed")
        selected_region_key = region_keys[region_names.index(selected_region_name)]
        cities = regions[selected_region_key].get('cities', [])
        
        # Build HTML Grid các thành phố
        html_cities = '<div class="city-grid">'
        for city in cities:
            c_name = city.get('name', '')
            # SỬA LỖI 2: Kéo link ảnh từ key 'img' trong JSON của bạn
            c_img = city.get('img', 'https://images.unsplash.com/photo-1522071820081-009f0129c71c') 
            
            html_cities += (
                f'<div class="city-card-premium">'
                f'<img src="{c_img}" class="city-bg-img" alt="{c_name}" loading="lazy">'
                f'<div class="city-overlay"></div>'
                f'<h3 class="city-name-title">{c_name}</h3>'
                f'</div>'
            )
            
        html_cities += (
            '</div>'
            '<div style="text-align: center; margin-top: 40px;">'
            f'<a href="/Destinations" target="_self" class="explore-btn">{D.get("cta_label", "Khám phá thêm")} <span class="arrow">→</span></a>'
            '</div>'
        )
        st.markdown(html_cities, unsafe_allow_html=True)

    # ==============================================================================
    # SECTION 2: WHY CHOOSE US & CEO QUOTE (NIỀM TIN KHÁCH HÀNG)
    # ==============================================================================
    features = [
        {"icon": "🌟", "title": "Trải Nghiệm Cao Cấp", "desc": "Mọi dịch vụ đều được tuyển chọn kỹ lưỡng, mang đến chất lượng 5 sao cho chuyến đi của bạn."},
        {"icon": "🛡️", "title": "An Tâm Tuyệt Đối", "desc": "Hỗ trợ 24/7 trong suốt hành trình, đảm bảo an toàn và xử lý rủi ro nhanh chóng."},
        {"icon": "💡", "title": "Thiết Kế Cá Nhân Hóa", "desc": "Lịch trình linh hoạt, thiết kế riêng theo sở thích và yêu cầu đặc biệt của bạn."},
        {"icon": "💎", "title": "Giá Trị Đích Thực", "desc": "Không phí ẩn, cam kết mang lại giá trị trải nghiệm vượt xa chi phí bạn bỏ ra."}
    ]
    
    html_about = (
        '<section class="feature-section">'
        '<div class="contained-content">'
        '<div class="feature-header">'
        '<span class="feature-label">VÌ SAO CHỌN VNWANDER</span>'
        '<h2 class="section-heading">Hành Trình Được Thiết Kế Bằng Đam Mê</h2>'
        '</div>'
        '<div class="feature-grid">'
    )
    for f in features:
        html_about += (
            f'<div class="feature-card">'
            f'<span class="feature-icon">{f["icon"]}</span>'
            f'<h3 class="feature-card-title">{f["title"]}</h3>'
            f'<p class="feature-card-desc">{f["desc"]}</p>'
            f'</div>'
        )
    html_about += '</div>'
    
    # CEO Quote chèn ngay dưới Why Choose Us
    if A.get('ceo_quote'):
        html_about += (
            '<div style="margin-top: 80px;">'
            '<div class="ceo-quote-box">'
            '<div class="quote-icon">"</div>'
            f'<p class="ceo-text">{A.get("ceo_quote", "")}</p>'
            f'<div class="ceo-author">{A.get("ceo_name", "")}</div>'
            f'<div class="ceo-title">{A.get("ceo_pos", "")}</div>'
            '</div></div>'
        )
    html_about += '</div></section>'
    st.markdown(html_about, unsafe_allow_html=True)

    # ==============================================================================
    # SECTION 3: REVIEWS (SOCIAL PROOF AUTO SCROLL)
    # ==============================================================================
    items = R.get('items', [])
    if items:
        # Nhân đôi list để animation scroll được mượt và vô tận
        display_items = items + items 
        html_reviews = (
            '<div class="reviews-section bg-light-grey">'
            '<div class="contained-content">'
            '<div class="feature-header">'
            '<span class="feature-label">CÂU CHUYỆN KHÁCH HÀNG</span>'
            f'<h2 class="section-heading">{R.get("title", "Khách Hàng Nói Gì Về Chúng Tôi")}</h2>'
            '</div>'
            '<div class="reviews-scroll-container">'
            '<div class="reviews-track">'
        )
        for item in display_items:
            stars = "⭐" * item.get('rating', 5)
            html_reviews += (
                f'<div class="review-card-vertical">'
                f'<div class="reviewer-meta">'
                f'<div class="reviewer-name">{item.get("name", "")}</div>'
                f'<div class="review-date">{item.get("date", "")}</div>'
                f'</div>'
                f'<div class="review-stars">{stars}</div>'
                f'<h3 class="review-testimonial-title">{item.get("testimonial", "")}</h3>'
                f'<p class="review-detailed-text">{item.get("detailed_review", "")}</p>'
                f'<a href="#" class="review-cta">{R.get("cta_label", "Xem chi tiết")} <span class="arrow">→</span></a>'
                f'</div>'
            )
        html_reviews += '</div></div></div></div>'
        st.markdown(html_reviews, unsafe_allow_html=True)

    render_footer()

if __name__ == "__main__":
    main()