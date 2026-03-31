import streamlit as st
from config.languages import CONTENT
from utils.helpers import get_local_img_url

def render_hero():
    """Renders the hero section"""
    # Fetch localized content
    L = CONTENT[st.session_state.lang]

    hero_bg = get_local_img_url("assets/images/hero.jpg")
    # Hero section HTML
    st.markdown(f"""
    <div class="hero-strip" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('{hero_bg}');">
        <div class="container hero-content">
            <p class="hero-eyebrow">{L['hero']['eyebrow']}</p>
            <h1 class="hero-title">
                {L['hero']['title_white']}<br>
                <span class="blue-text">{L['hero']['title_blue']}</span>
            </h1>
            <p class="hero-subtitle">{L['hero']['subtitle']}</p>
            <a href="#" class="btn-cta">
                {L['hero']['cta']} <span class="arrow">→</span>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)