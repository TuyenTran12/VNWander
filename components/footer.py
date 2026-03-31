import streamlit as st
from config.languages import CONTENT

def render_navbar():
    # Nạp Font Awesome để hiện Icon
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

def render_footer():
    lang = st.session_state.get('lang', 'vi')
    L = CONTENT.get(lang, {})
    F = L.get('footer', {})

    # Dòng khai báo biến THỤT VÀO 4 dấu cách (đúng luật Python)
    # Nhưng nội dung bên dưới PHẢI nằm sát lề trái (đúng luật Markdown)
    footer_html = f"""
<div class="vn-footer">
<div class="contained-content">
<div class="footer-grid">
<div class="footer-col">
<h4><i class="fa-solid fa-building"></i> {F.get('headquarters', 'Trụ sở')}</h4>
<p><i class="fa-solid fa-phone"></i> <strong>{F.get('hotline', '1900 ****')}</strong></p>
<p><i class="fa-solid fa-envelope"></i> {F.get('email', 'hotro@vnwander.vn')}</p>
<p><i class="fa-solid fa-location-dot"></i> {F.get('address', '')}</p>
</div>

<div class="footer-col">
<h4>{F.get('presence_title', 'Địa điểm')}</h4>
<ul>
{''.join([f"<li><i class='fa-solid fa-chevron-right' style='font-size:0.7rem;'></i> {city}</li>" for city in F.get('cities', [])])}
</ul>
</div>

<div class="footer-col">
<h4>{F.get('connect_title', 'Kết nối')}</h4>
<p style="font-size: 0.85rem; color: #A0A0A0;">{F.get('connect_desc', '')}</p>
<div class="social-icons">
<a href="#"><i class="fa-brands fa-facebook"></i></a>
<a href="#"><i class="fa-brands fa-instagram"></i></a>
<a href="#"><i class="fa-brands fa-linkedin"></i></a>
<a href="#"><i class="fa-brands fa-youtube"></i></a>
</div>
</div>

<div class="footer-col">
<h4>{F.get('legal_title', 'Hỗ trợ')}</h4>
<ul>
{''.join([f"<li>{link}</li>" for link in F.get('legal_links', [])])}
</ul>
</div>

<div class="footer-col">
<h4>{F.get('brands_title', 'Hệ sinh thái')}</h4>
<ul>
{''.join([f"<li>{brand}</li>" for brand in F.get('brands', [])])}
</ul>
</div>
</div>

<div class="footer-bottom">
<p>{F.get('copyright', '© 2026 VNWANDER. All Rights Reserved.')}</p>
</div>
</div>
</div>
"""
    st.markdown(footer_html, unsafe_allow_html=True)