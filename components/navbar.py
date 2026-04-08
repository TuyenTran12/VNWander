import streamlit as st
from config.languages import CONTENT

_SIDEBAR_LINKS = [
    ("team",   "👥", "/Team"),
    ("career", "💼", "/Careers"),
    ("news",   "📰", "/News"),
]

def render_navbar(current_page_path: str = "/") -> None:
    lang = st.session_state.get("lang", "vi")
    # Safely get language data, fallback to Vietnamese
    L = CONTENT.get(lang, CONTENT.get("vi")) 
    next_lang  = "en" if lang == "vi" else "vi"
    lang_label = "EN" if lang == "vi" else "VI"

    nav            = L.get("navbar", {})
    login_label    = nav.get("login",    "Login")
    register_label = nav.get("register", "Register")
    explore_label  = nav.get("explore",  "Explore")

    sidebar_links_html = "".join(
        f'<a href="{path}?lang={lang}" class="vn-sidebar-link{" active" if current_page_path.rstrip("/") == path.rstrip("/") else ""}" target="_self">'
        f'<span class="vn-link-icon">{icon}</span>{nav.get(key, key.capitalize())}'
        f'</a>\n'
        for key, icon, path in _SIDEBAR_LINKS
    )

    # ── CSS CHECKBOX HACK (NO JS REQUIRED) ───────────────────────────────
    html = f"""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">

    <style>
        /* Hide the toggle checkbox */
        #vnToggleSidebar {{
            display: none !important;
        }}

        /* Logic: Open menu when checkbox is checked */
        #vnToggleSidebar:checked ~ .vn-overlay {{
            opacity: 1 !important;
            visibility: visible !important;
            pointer-events: auto !important;
        }}
        
        #vnToggleSidebar:checked ~ .vn-sidebar {{
            transform: translateX(0) !important;
        }}

        /* Default state (Menu closed) */
        .vn-overlay {{
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: all 0.3s ease;
        }}
        
        .vn-sidebar {{
            transform: translateX(-100%);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
    </style>

    <div class="vn-navbar-wrapper">
        
        <input type="checkbox" id="vnToggleSidebar">

        <label class="vn-overlay" for="vnToggleSidebar"></label>

        <nav class="vn-sidebar" aria-label="Site navigation">
            <div class="vn-sidebar-header">
                <a href="/?lang={lang}" class="vn-sidebar-brand" target="_self">VNWander</a>
                <label class="vn-sidebar-close" for="vnToggleSidebar" aria-label="Close menu" style="cursor: pointer;">&#x2715;</label>
            </div>
            
            <div class="vn-sidebar-nav">
                <p class="vn-sidebar-label">{explore_label}</p>
                {sidebar_links_html}
                <div class="vn-sidebar-divider"></div>
            </div>
            
            <div class="vn-sidebar-footer">
                <a href="/login?lang={lang}" class="vn-btn vn-btn-login" target="_self">{login_label}</a>
                <a href="/register?lang={lang}" class="vn-btn vn-btn-register" target="_self">{register_label}</a>
            </div>
        </nav>

        <header class="vn-navbar" role="banner">
            <div class="vn-navbar-inner">
                <div class="vn-nav-left">
                    <label class="vn-hamburger" for="vnToggleSidebar" style="cursor: pointer;">
                        <span></span><span></span><span></span>
                    </label>
                </div>
                
                <div class="vn-nav-center">
                    <a href="/?lang={lang}" class="vn-logo" target="_self">VNWander</a>
                </div>
                
                <div class="vn-nav-right">
                    <a href="{current_page_path}?lang={next_lang}" class="vn-lang-btn" target="_self">{lang_label}</a>
                </div>
            </div>
        </header>
    </div>
    """

    # Clean up leading spaces to prevent Streamlit from rendering HTML as Markdown code blocks
    clean_html = "\n".join([line.strip() for line in html.split("\n")])
    st.markdown(clean_html, unsafe_allow_html=True)