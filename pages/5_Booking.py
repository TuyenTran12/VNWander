import streamlit as st
import os
from config.languages import CONTENT
from utils.helpers import get_local_img_url
from utils.session_init import init_session_state

# Load external CSS
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize page configuration
st.set_page_config(page_title="VNWander | Book Tickets", layout="wide")
init_session_state()

# Fetch localized content
L = CONTENT[st.session_state.lang]

# Apply styles
load_css("assets/css/style.css")

# Render navigation bar using component (consistent with other pages)
from components.navbar import render_navbar
render_navbar()

# Render Language Toggle Button
st.markdown('<div class="lang-button-container">', unsafe_allow_html=True)
if st.button("ENG" if st.session_state.lang == 'vi' else "VIE", key="lang-toggle"):
    st.session_state.lang = 'en' if st.session_state.lang == 'vi' else 'vi'
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Booking Form Section
st.markdown(f"""
<div class="booking-search-bar">
    <div class="booking-container">
        <div class="booking-title">{L['booking']['title']}</div>
        <form class="booking-form">
            <div class="form-group">
                <label for="destination">{L['booking']['destination']}</label>
                <select id="destination">
                    <option value="">-- {L['booking']['select_destination']} --</option>
                    <option value="">Hà Nội</option>
                    <option value="">Hồ Chí Minh</option>
                    <option value="">Đà Nẵng</option>
                    <option value="">Nha Trang</option>
                    <option value="">Phú Quốc</option>
                    <option value="">Đà Lạt</option>
                </select>
            </div>
            <div class="form-group">
                <label for="checkin">{L['booking']['checkin']}</label>
                <input type="date" id="checkin" name="checkin">
            </div>
            <div class="form-group">
                <label for="checkout">{L['booking']['checkout']}</label>
                <input type="date" id="checkout" name="checkout">
            </div>
            <div class="form-group guests">
                <label for="guests">{L['booking']['guests']}</label>
                <select id="guests" name="guests">
                    <option value="1">1 {L['booking']['guest']}</option>
                    <option value="2">2 {L['booking']['guests_plural']}</option>
                    <option value="3">3 {L['booking']['guests_plural']}</option>
                    <option value="4">4+ {L['booking']['guests_plural']}</option>
                </select>
            </div>
            <button type="submit" class="search-btn">{L['booking']['search_button']}</button>
        </form>
    </div>
</div>
""", unsafe_allow_html=True)