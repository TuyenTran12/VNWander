import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from utils.helpers import load_css
from utils.session_init import init_session_state

# Set page configuration
st.set_page_config(
    page_title="VNWander - Contact Us",
    page_icon="📞",
    layout="wide"
)
init_session_state()

# Load custom CSS
load_css("assets/css/style.css")

# Render navigation bar
render_navbar()

# Page content
st.title("Liên hệ / Contact Us")
st.write("This is the placeholder content for the Contact page.")
st.write("In a real implementation, this would contain contact information and a form.")

# Render footer
render_footer()