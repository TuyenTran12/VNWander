# utils/session_init.py
import streamlit as st

def init_session_state():
    """Initialize session state variables if they don't exist."""
    if 'lang' not in st.session_state:
        st.session_state.lang = 'vi'
    if 'selected_region' not in st.session_state:
        st.session_state.selected_region = 'north'
    if 'selected_city' not in st.session_state:
        st.session_state.selected_city = None