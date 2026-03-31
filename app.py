import streamlit as st
import os
from utils.helpers import get_local_img_url

from components.navbar import render_navbar
from components.hero import render_hero
from components.footer import render_footer
from config.languages import CONTENT

# Load external CSS
def load_all_css():
    css_files = [
        "assets/css/base.css",
        "assets/css/navbar.css",
        "assets/css/hero.css",
        "assets/css/components.css",
        "assets/css/footer.css"
    ]

    combined_css = ""
    for css_file in css_files:
        if os.path.exists(css_file):
            with open(css_file, encoding="utf-8") as f:
                combined_css += f.read() + "\n\n"

    if combined_css:
        st.markdown(f'<style>{combined_css}</style>', unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="VNWander",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read query params to keep UI in sync with URL
query_params = st.query_params
if "lang" in query_params:
    st.session_state.lang = query_params["lang"]
if "region" in query_params:
    st.session_state.selected_region = query_params["region"]

# Initialize language in session state if not present
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

# Define L correctly
L = CONTENT[st.session_state.lang]

# Load CSS
load_all_css()

# Render navbar
render_navbar()

# Render hero section
render_hero()

# ===== Favorite Destinations Section =====
DEST = L['destinations']

# Initialize selected region in session state if not present
if 'selected_region' not in st.session_state:
    st.session_state.selected_region = list(DEST['regions'].keys())[0]

current_region = st.session_state.selected_region

# 1. Render Title & Subtitle (Căn giữa, Title xanh, Subtitle đen)
st.markdown(f"""
<div class="dest-section" style="text-align: center; margin-top: 60px; margin-bottom: 40px; padding: 0 20px;">
    <h1 style="color: #0056A3; font-size: 2.8rem; font-family: 'Playfair Display', serif; font-weight: 700; margin-bottom: 15px;">{DEST['title']}</h1>
    <p style="color: #000000; font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.6;">{DEST['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 2. RENDER REGION TABS (DÙNG CALLBACK CHỐNG XUNG ĐỘT STATE)
# =========================================================
regions_data = DEST.get('regions', {})
options = list(regions_data.keys())

# Lấy miền hiện tại từ URL (nếu có), nếu không thì mặc định là miền đầu tiên
if "region" in st.query_params and st.query_params["region"] in options:
    current_val = st.query_params["region"]
else:
    current_val = options[0] if options else ""

# HÀM CALLBACK: Kích hoạt ngay chớp mắt khi người dùng vừa click chuột
def on_region_change():
    # Cập nhật URL ngầm ngay lập tức theo nút Radio vừa bấm
    st.query_params["region"] = st.session_state.region_radio_widget

# Tính toán vị trí đang đứng
current_index = options.index(current_val) if current_val in options else 0

# Vẽ Tabs (Radio) và gắn hàm Callback vào
selected_region = st.radio(
    "Chọn miền",
    options=options,
    format_func=lambda x: regions_data[x].get('label', x),
    index=current_index,
    horizontal=True,
    label_visibility="collapsed",
    key="region_radio_widget",  # Key độc nhất
    on_change=on_region_change  # ĐÂY LÀ CHÌA KHÓA: Gọi hàm đồng bộ ngay khi click
)

# =========================================================
# 3. RENDER CITY CARDS GRID (LẤY ĐÚNG MIỀN VỪA CHỌN)
# =========================================================
# Lấy danh sách thành phố chuẩn 100% từ biến selected_region
cities = regions_data.get(selected_region, {}).get('cities', [])

city_html = '<div class="city-grid">\n'

for city_item in cities:
    city_name = city_item['name']    
    
    main_img_url = city_item['img'].strip()  
    
    img_name = city_name.lower().replace(' ', '-').replace('.', '')
    
    city_html += f"""
<div class="city-card-premium">
    <img class="city-bg-img" src="{main_img_url}" loading="lazy" decoding="async" alt="{city_name}" />
    <div class="city-overlay"></div>
    
    <div class="city-decor-grid">
        <div class="decor-item" style="background-image: url('https://picsum.photos/seed/{img_name}1/100/100');"></div>
        <div class="decor-item" style="background-image: url('https://picsum.photos/seed/{img_name}2/100/100');"></div>
        <div class="decor-item" style="background-image: url('https://picsum.photos/seed/{img_name}3/100/100');"></div>
        <div class="decor-item" style="background-image: url('https://picsum.photos/seed/{img_name}4/100/100');"></div>
    </div>
    
<h3 class="city-name-title">{city_name}</h3>
</div>
"""
city_html += '</div>'

# In toàn bộ Grid Thành phố ra bằng 1 lệnh duy nhất
st.markdown(city_html, unsafe_allow_html=True)

# ===== Reviews section =====
reviews = CONTENT[st.session_state.lang]['reviews']
items = reviews['items']
display_items = items + items 

# 1. Nén toàn bộ các thẻ con (Cards) thành 1 dòng dài duy nhất bằng hàm join()
cards_html = "".join([
    f"""<div class="review-card-vertical"><div class="reviewer-meta"><div class="reviewer-name">{item['name']}</div><div class="review-date">{item['date']}</div></div><div class="review-stars">{"⭐" * item['rating']}</div><h3 class="review-testimonial-title">{item['testimonial']}</h3><p class="review-detailed-text">{item['detailed_review']}</p><a href="#" class="review-cta">{reviews['cta_label']} <span class="arrow">→</span></a></div>"""
    for item in display_items
])

# 2. Nén toàn bộ khung cha bên ngoài thành 1 dòng và nhét thẻ con vào giữa
reviews_html = f"""<div class="reviews-section bg-light-grey"><div class="contained-content"><div class="reviews-header"><div class="section-label">{reviews['label']}</div><h2 class="section-title">{reviews['title']}</h2></div><div class="reviews-scroll-container"><div class="reviews-track">{cards_html}</div></div></div></div>"""

# 3. In ra màn hình (Lúc này HTML là 1 khối đặc nguyên khối, Streamlit không thể phá)
st.markdown(reviews_html, unsafe_allow_html=True)

render_footer()