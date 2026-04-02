import streamlit as st
import os
import datetime
from utils.helpers import get_local_img_url
from components.navbar import render_navbar
from components.search_bar import render_search_bar
from components.hero import render_hero
from components.footer import render_footer
from config.languages_home import CONTENT

# ------------------------------------------------------------------------------
# Helper: Extract all cities from the destination data
# ------------------------------------------------------------------------------
def get_all_cities(destinations_data):
    cities = set()
    for region in destinations_data.get('regions', {}).values():
        for city in region.get('cities', []):
            cities.add(city['name'])
    return sorted(list(cities))

# ------------------------------------------------------------------------------
# MAIN APP ENTRY POINT
# ------------------------------------------------------------------------------
def main():
    # Configure main page layout
    st.set_page_config(page_title="VNWander - Khám Phá Việt Nam", layout="wide", initial_sidebar_state="collapsed")
    
    # Load and combine all external CSS files dynamically
    css_files = ["assets/css/base.css", "assets/css/navbar.css", "assets/css/hero.css", "assets/css/components.css", "assets/css/footer.css", "assets/css/style.css"]
    combined_css = ""
    for css_file in css_files:
        if os.path.exists(css_file):
            with open(css_file, encoding="utf-8") as f:
                combined_css += f.read() + "\n\n"
    if combined_css:
        st.markdown(f"<style>{combined_css}</style>", unsafe_allow_html=True)

    # Initialize localization (i18n) from URL params or default to Vietnamese
    if "lang" in st.query_params:
        st.session_state.lang = st.query_params["lang"]
    elif 'lang' not in st.session_state:
        st.session_state.lang = 'vi'
    lang = st.session_state.lang
    
    # ── RENDER HEADER & HERO ───────────────────────────────────────────────────
    render_navbar(current_page_path="/")
    render_hero()
    
    # Wrap Search bar in a container to push it up over the Hero section via CSS
    st.markdown('<div class="premium-search-wrapper">', unsafe_allow_html=True)
    #render_search_bar()
    st.markdown('</div>', unsafe_allow_html=True)

    # ── FETCH CONTENT DATA BASED ON SELECTED LANGUAGE ──────────────────────────
    D = CONTENT[lang].get('destinations', {})
    A = CONTENT[lang].get('about', {})
    R = CONTENT[lang].get('reviews', {})
    F = CONTENT[lang].get('features', {})

    # ==============================================================================
    # SECTION 1: FAVORITE DESTINATIONS (4-COLUMN GRID)
    # ==============================================================================
    st.markdown(
        '<div class="section-heading-container">'
        f'<span class="feature-label">{D.get("explore_label", "KHÁM PHÁ VIỆT NAM")}</span>'
        f'<h2 class="section-heading">{D.get("title", "Điểm đến yêu thích")}</h2>'
        '</div>', 
        unsafe_allow_html=True
    )

    regions = D.get('regions', {})
    if regions:
        region_keys = list(regions.keys())
        
        # Extract region names safely using the 'label' key
        region_names = [regions[k].get('label', k) for k in region_keys]
        
        # Region selection tabs
        selected_region_name = st.radio("Choose Region", region_names, horizontal=True, label_visibility="collapsed")
        selected_region_key = region_keys[region_names.index(selected_region_name)]
        cities = regions[selected_region_key].get('cities', [])
        
        # Build HTML Grid for cities 
        html_cities = '<div class="city-grid">'
        for city in cities:
            c_name = city.get('name', '')
            # Ensure fallback image URL is provided to prevent KeyError crashes
            c_img = city.get('img', 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800') 
            
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
            f'<a href="/Destinations" target="_self" class="explore-btn">{D.get("cta_label", "Explore More")} <span class="arrow">→</span></a>'
            '</div>'
        )
        st.markdown(html_cities, unsafe_allow_html=True)

    # ==============================================================================
    # SECTION 2: WHY CHOOSE US & CEO QUOTE (FULLY BILINGUAL)
    # ==============================================================================
    html_about = (
        '<section class="feature-section">'
        '<div class="contained-content">'
        '<div class="feature-header">'
        f'<span class="feature-label">{F.get("eyebrow", "VÌ SAO CHỌN VNWANDER")}</span>'
        f'<h2 class="section-heading">{F.get("title", "Hành Trình Được Thiết Kế Bằng Đam Mê")}</h2>'
        '</div>'
        '<div class="feature-grid">'
    )
    
    # Iterate over features list from language file
    for f_item in F.get('items', []):
        html_about += (
            f'<div class="feature-card">'
            f'<span class="feature-icon">{f_item.get("icon", "🌟")}</span>'
            f'<h3 class="feature-card-title">{f_item.get("title", "")}</h3>'
            f'<p class="feature-card-desc">{f_item.get("desc", "")}</p>'
            f'</div>'
        )
    html_about += '</div>'
    
    # ── CEO QUOTE: LARGE IMAGE ON THE LEFT, TEXT ON THE RIGHT ──
    if A.get('ceo_quote'):
        html_about += (
            '<div style="margin-top: 80px;">'
            '<div class="ceo-quote-box" style="display: flex; flex-direction: row; align-items: center; gap: 50px; text-align: left; padding: 50px; background: #f8faff; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">'
                
                # Left Column: Large CEO Image (200px)
                '<div style="flex-shrink: 0;">'
                    f'<img src="{A.get("ceo_img", "https://randomuser.me/api/portraits/men/32.jpg")}" style="width: 200px; height: 200px; border-radius: 20px; object-fit: cover; box-shadow: 0 15px 35px rgba(0,86,163,0.15); border: 4px solid #ffffff;">'
                '</div>'
                
                # Right Column: Quote content and author info
                '<div style="flex: 1;">'
                    '<div class="quote-icon" style="position: static; font-size: 5rem; color: #dbeafe; line-height: 0.8; margin-bottom: 10px; font-family: serif;">"</div>'
                    f'<p class="ceo-text" style="font-size: 1.25rem; line-height: 1.8; color: #222; font-style: italic; margin-bottom: 25px;">{A.get("ceo_quote", "")}</p>'
                    f'<div class="ceo-author" style="font-size: 1.4rem; font-weight: 800; color: #0056A3;">{A.get("ceo_name", "")}</div>'
                    f'<div class="ceo-title" style="font-size: 0.9rem; color: #666; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; margin-top: 5px;">{A.get("ceo_pos", "")}</div>'
                '</div>'
                
            '</div></div>'
        )
    html_about += '</div></section>'
    st.markdown(html_about, unsafe_allow_html=True)

    # ==============================================================================
    # SECTION 3: SOCIAL PROOF (REVIEWS WITH INFINITE AUTO-SCROLL)
    # ==============================================================================
    items = R.get('items', [])
    if items:
        # Duplicate the items list to ensure seamless infinite scrolling CSS animation
        display_items = items + items 
        html_reviews = (
            '<div class="reviews-section bg-light-grey">'
            '<div class="contained-content">'
            '<div class="feature-header">'
            f'<span class="feature-label">{R.get("label", "CÂU CHUYỆN KHÁCH HÀNG")}</span>'
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

    # ── RENDER FOOTER ──────────────────────────────────────────────────────────
    render_footer()

if __name__ == "__main__":
    main()