import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from utils.helpers import load_all_global_css
from utils.session_init import init_session_state
from config.languages import CONTENT

# 1. Cấu hình trang (Luôn ở dòng đầu tiên)
st.set_page_config(page_title="VNWander - Đội Ngũ", layout="wide")
init_session_state()
load_all_global_css()

if "lang" in st.query_params:
    st.session_state.lang = st.query_params["lang"]
elif 'lang' not in st.session_state:
    st.session_state.lang = 'vi'

# 2. Render Navbar
render_navbar(current_page_path="/Team")

# 3. Lấy dữ liệu ngôn ngữ
lang = st.session_state.get('lang', 'vi')
T = CONTENT.get(lang, {}).get('team_page', {})

# 4. KHỐI HTML (LƯU Ý: Không thụt đầu dòng các thẻ DIV)
team_content = f"""
<div class="contained-content" style="padding-top: 100px;">

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; margin-bottom: 80px;">
<div class="team-info-box">
<h2 style="color: #0056A3; font-family: 'Playfair Display', serif; font-size: 2.5rem;">{T.get('section1_title', 'NHÂN LỰC TẬN TÂM')}</h2>
<p style="font-size: 1.1rem; line-height: 1.8; color: #444; text-align: justify;">{T.get('section1_text', '')}</p>
</div>
<div class="team-img-box">
<img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800" style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; margin-bottom: 80px;">
<div class="team-img-box" style="order: 1;">
<img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800" style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
</div>
<div class="team-info-box" style="order: 2;">
<h2 style="color: #0056A3; font-family: 'Playfair Display', serif; font-size: 2.5rem;">{T.get('section2_title', 'PHÁT TRIỂN TÀI NĂNG')}</h2>
<p style="font-size: 1.1rem; line-height: 1.8; color: #444; text-align: justify;">{T.get('section2_text', '')}</p>
</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; margin-bottom: 80px;">
<div class="team-info-box">
<h2 style="color: #0056A3; font-family: 'Playfair Display', serif; font-size: 2.5rem;">{T.get('section3_title', 'TẦM NHÌN LÃNH ĐẠO')}</h2>
<p style="font-size: 1.1rem; line-height: 1.8; color: #444; text-align: justify;">{T.get('section3_text', '')}</p>
</div>
<div class="team-img-box">
<img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800" style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
</div>
</div>

</div>
"""

# Render ra giao diện
st.markdown(team_content, unsafe_allow_html=True)

# 5. Render Footer
render_footer()