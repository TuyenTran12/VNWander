import streamlit as st
import datetime
from config.languages import CONTENT
from utils.session_init import init_session_state
from utils.helpers import load_all_global_css  # Import hàm load CSS
from components.navbar import render_navbar
from components.footer import render_footer

# 1. Khởi tạo trang
st.set_page_config(page_title="VNWander | Book Tickets", layout="wide")
init_session_state()

# Load toàn bộ CSS (Giúp kết nối với file CSS vừa tách)
load_all_global_css()

# 2. Xử lý ngôn ngữ đồng bộ với URL
if "lang" in st.query_params:
    st.session_state.lang = st.query_params["lang"]
elif 'lang' not in st.session_state:
    st.session_state.lang = 'vi'

# Sử dụng .get() để lấy dữ liệu an toàn
L = CONTENT.get(st.session_state.lang, {})
B = L.get('booking', {}) 

# Render Navbar
render_navbar(current_page_path="/Booking")

# 3. Lấy ngày hiện tại và ngày mai bằng Python
today = datetime.date.today().strftime("%Y-%m-%d")
tomorrow = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%Y-%m-%d")

# 4. KHỐI HTML (Đã được dọn dẹp sạch sẽ CSS)
booking_html = f"""
<div class="booking-wrapper">
<div class="booking-box">
<div class="booking-title">{B.get('title', 'Tìm chuyến bay & Đặt phòng')}</div>

<form class="booking-form">
<div class="trip-type-options">
<label><input type="radio" name="trip_type" checked> {B.get('round_trip', 'Khứ hồi')}</label>
<label><input type="radio" name="trip_type"> {B.get('one_way', 'Một chiều')}</label>
</div>

<div class="form-grid">
<div class="form-group">
<label>{B.get('from', 'Điểm khởi hành')}</label>
<select>
<option value="SGN">Hồ Chí Minh (SGN)</option>
<option value="HAN">Hà Nội (HAN)</option>
<option value="DAD">Đà Nẵng (DAD)</option>
<option value="PQC">Phú Quốc (PQC)</option>
</select>
</div>

<div class="form-group">
<label>{B.get('to', 'Điểm đến')}</label>
<select>
<option value="HAN">Hà Nội (HAN)</option>
<option value="SGN">Hồ Chí Minh (SGN)</option>
<option value="DAD">Đà Nẵng (DAD)</option>
<option value="DLI">Đà Lạt (DLI)</option>
</select>
</div>

<div class="form-group">
<label>{B.get('depart_date', 'Ngày đi')}</label>
<input type="date" value="{today}">
</div>

<div class="form-group" style="grid-column: span 2;">
<label>{B.get('passengers_class', 'Hành khách & Hạng ghế')}</label>
<select>
<option>1 {B.get('adult', 'Người lớn')}, Phổ thông</option>
<option>2 {B.get('adult', 'Người lớn')}, Phổ thông</option>
<option>1 {B.get('adult', 'Người lớn')}, Thương gia</option>
<option>Gia đình (4+ người)</option>
</select>
</div>

<div class="search-btn-wrapper">
<button type="button" class="search-btn">{B.get('search_btn', 'TÌM CHUYẾN ĐI')}</button>
</div>
</div>
</form>
</div>
</div>
"""

st.markdown(booking_html, unsafe_allow_html=True)
render_footer()