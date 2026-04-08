import streamlit as st
from components.ai_widget import render_chat_widget
from components.navbar import render_navbar
from components.footer import render_footer
from utils.helpers import load_all_global_css
from utils.session_init import init_session_state
from config.languages import CONTENT

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="VNWander - Đội ngũ", layout="wide")
init_session_state()
load_all_global_css()

# ── Language ────────────────────────────────────────────────────────────────────
if "lang" in st.query_params:
    st.session_state.lang = st.query_params["lang"]
elif "lang" not in st.session_state:
    st.session_state.lang = "vi"

lang = st.session_state.lang
T = CONTENT[lang].get("team_page", {})

# ── Navbar ──────────────────────────────────────────────────────────────────────
render_navbar(current_page_path="/Team")


# ==============================================================================
# SECTION 1 — HERO / HOOK
# Single st.markdown call: all HTML pre-built into one string.
# ==============================================================================
hook_title    = T.get("hook_title", "Những con người đằng sau những hành trình trong mơ")
hook_subtitle = T.get("hook_subtitle", "Chúng tôi không chỉ là nhân viên văn phòng — chúng tôi là những người đam mê du lịch, "
                      "những chuyên gia địa phương đã đặt chân đến mọi ngóc ngách của Việt Nam. "
                      "Mỗi hành trình chúng tôi thiết kế đều mang theo câu chuyện thực của chính mình.")
hero_eyebrow  = T.get("hero_eyebrow", "Gặp gỡ đội ngũ của chúng tôi")

html_hero = f"""
<section class="team-hero">
    <div class="team-hero-bg"></div>
    <div class="team-hero-inner">
        <span class="team-eyebrow">{hero_eyebrow}</span>
        <h1 class="team-hero-title">{hook_title}</h1>
        <p class="team-hero-subtitle">{hook_subtitle}</p>
        <div class="team-hero-divider">
            <span></span>
            <i>✦</i>
            <span></span>
        </div>
    </div>
</section>
"""
st.markdown(html_hero, unsafe_allow_html=True)


# ==============================================================================
# SECTION 2 — LEADERSHIP VISION
# ==============================================================================
leadership       = T.get("leadership", {})
leader_eyebrow   = T.get("leader_eyebrow", "Ban Lãnh đạo")

# Safely pull the first leader from the list (if data exists)
leader = {}
if leadership.get("members"):
    leader = leadership["members"][0]

leader_img   = leader.get("image", "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=600&q=80")
leader_name  = leader.get("name", "Nguyễn Minh Tuấn")
leader_title = leader.get("role", "Nhà sáng lập & CEO")
leader_quote = leader.get("quote", "Mỗi chuyến đi là một cơ hội để thay đổi cách nhìn về thế giới — "
                           "và sứ mệnh của VNWander là trao cho bạn cơ hội đó một cách trọn vẹn nhất.")

html_leadership = f"""
<section class="team-leadership">
<div class="team-page-wrap">
<div class="team-leadership-grid">

<div class="team-leader-photo-wrap">
<img src="{leader_img}" alt="{leader_name}" loading="lazy">
</div>

<div class="team-leader-content">
<span class="team-eyebrow">{leader_eyebrow}</span>
<h2 class="team-leader-name">{leader_name}</h2>
<p class="team-leader-title">{leader_title}</p>
<div class="team-leader-quote">
<span class="team-leader-quote-mark">&ldquo;</span>
<p>{leader_quote}</p>
</div>
</div>

</div>
</div>
</section>
"""
st.markdown(html_leadership, unsafe_allow_html=True)


# ==============================================================================
# SECTION 3 — CORE TEAM (3 groups · 2-col CSS Grid per group)
# ==============================================================================
core_teams    = T.get("core_teams", {})
core_eyebrow  = T.get("core_eyebrow", "Đội ngũ chuyên nghiệp")
core_title    = T.get("core_title", "Đội ngũ nòng cốt của VNWander")
core_subtitle = T.get("core_subtitle", "Ba bộ phận — một mục tiêu: mang đến cho bạn những hành trình không thể quên.")

GROUP_ICONS = ["🗺️", "🌿", "💻"]

html_core = (
    '<div class="core-teams-section"><div class="core-teams-container">'
    '<div class="team-core-header" style="text-align: center; margin-bottom: 50px;">'
    f'<span class="team-eyebrow" style="color: #4CB5F9; font-weight: 700; text-transform: uppercase;">{core_eyebrow}</span>'
    f'<h2 style="font-family: \'Playfair Display\', serif; font-size: 2.5rem; color: #0056A3; margin-top: 10px;">{core_title}</h2>'
    f'<p style="color: #666; max-width: 700px; margin: 20px auto 0 auto;">{core_subtitle}</p>'
    '</div>'
)

if core_teams.get('groups'):
    for idx, group in enumerate(core_teams['groups']):
        group_name = group.get('group_name', '')
        group_desc = group.get('desc', '')
        current_icon = GROUP_ICONS[idx] if idx < len(GROUP_ICONS) else "⭐"

        html_core += (
            f'<div class="team-group" style="margin-bottom: 60px;">'
            f'<div class="team-group-header" style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">'
            f'<div class="team-group-icon" style="font-size: 2rem;">{current_icon}</div>'
            f'<h3 class="team-group-name" style="font-size: 1.8rem; color: #0056A3; margin: 0;">{group_name}</h3>'
            f'</div>'
            f'<p class="team-group-desc" style="color: #444; margin-bottom: 30px;">{group_desc}</p>'
            f'<div class="team-members-grid">'
        )
        
        for member in group.get('members', []):
            m_img  = member.get('image', 'https://via.placeholder.com/300x400')
            m_name = member.get('name', '')
            m_role = member.get('role', '')
            m_bio  = member.get('bio', '')

            # Gắn card thành viên bằng một khối liền mạch, chống lộ code
            html_core += (
                f'<div class="member-card">'
                f'<div class="member-photo"><img src="{m_img}" alt="{m_name}" loading="lazy"></div>'
                f'<div class="member-body">'
                f'<div class="member-info"><p class="member-name">{m_name}</p><p class="member-role">{m_role}</p></div>'
                f'<span class="member-fun-fact">{m_bio}</span>'
                f'</div></div>'
            )
            
        html_core += '</div></div>'

html_core += '</div></div>'
st.markdown(html_core, unsafe_allow_html=True)

# ==============================================================================
# SECTION 4 — BEHIND THE SCENES (Culture)
# ==============================================================================
culture         = T.get("culture", {})
culture_eyebrow = T.get("culture_eyebrow", "Văn hóa công ty")
culture_title   = culture.get("title", "Gia đình VNWander")
culture_desc    = culture.get("desc",
    "Chúng tôi tin rằng một đội ngũ hạnh phúc tạo nên những hành trình hạnh phúc. "
    "Đây là góc nhìn phía sau hậu trường — nơi những kế hoạch táo bạo được sinh ra "
    "trong tiếng cười và cốc cà phê buổi sáng.")

# Pull up to 3 culture images; fall back to curated Unsplash URLs
default_culture_imgs = [
    ("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",  "Họp nhóm sáng tạo"),
    ("https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=600&q=80",  "Chuyến khảo sát thực địa"),
    ("https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?auto=format&fit=crop&w=600&q=80",  "Team building cuối năm"),
]
raw_imgs = culture.get("images", [])
culture_imgs = []
for i, (default_url, caption) in enumerate(default_culture_imgs):
    url = raw_imgs[i] if i < len(raw_imgs) else default_url
    culture_imgs.append((url, caption))

# Culture value pillars (from T dict or sensible defaults)
value_items = T.get("culture_values", [
    {"icon": "🤝", "title": "Gia đình trước tiên",  "desc": "Mọi quyết định đều đặt con người lên hàng đầu."},
    {"icon": "🌏", "title": "Tò mò không giới hạn", "desc": "Chúng tôi không ngừng khám phá và học hỏi."},
    {"icon": "💡", "title": "Sáng tạo thực tiễn",   "desc": "Ý tưởng hay nhất thường đến từ hành trình thực tế."},
])

# Build photo mosaic HTML (large left image spans 2 rows, 2 smaller right)
photos_html = f"""
<div class="culture-photo large">
    <img src="{culture_imgs[0][0]}" alt="{culture_imgs[0][1]}" loading="lazy">
    <div class="culture-photo-caption">{culture_imgs[0][1]}</div>
</div>
<div class="culture-photo">
    <img src="{culture_imgs[1][0]}" alt="{culture_imgs[1][1]}" loading="lazy">
    <div class="culture-photo-caption">{culture_imgs[1][1]}</div>
</div>
<div class="culture-photo">
    <img src="{culture_imgs[2][0]}" alt="{culture_imgs[2][1]}" loading="lazy">
    <div class="culture-photo-caption">{culture_imgs[2][1]}</div>
</div>"""

values_html = "".join(f"""
<div class="culture-value">
    <div class="culture-value-icon">{v['icon']}</div>
    <h4>{v['title']}</h4>
    <p>{v['desc']}</p>
</div>""" for v in value_items)

html_culture = f"""
<section class="team-culture">
    <div class="team-page-wrap">
        <div class="team-culture-header">
            <span class="team-eyebrow">{culture_eyebrow}</span>
            <h2>{culture_title}</h2>
            <div class="team-section-divider"></div>
            <p style="margin-top:20px">{culture_desc}</p>
        </div>
        <div class="team-culture-gallery">
            {photos_html}
        </div>
        <div class="team-culture-values">
            {values_html}
        </div>
    </div>
</section>
"""
st.markdown(html_culture, unsafe_allow_html=True)


# ==============================================================================
# SECTION 5 — CALL TO ACTION
# ==============================================================================
cta = T.get("cta", {})

cta_eyebrow      = T.get("cta_eyebrow", "Tiếp theo")
cta_title        = cta.get("booking_title", "Sẵn sàng cho hành trình tiếp theo?")
cta_subtitle     = cta.get("subtitle",
    "Dù bạn muốn khám phá hay muốn cùng chúng tôi tạo nên những chuyến đi ý nghĩa — "
    "chúng tôi luôn chào đón bạn.")
booking_btn_text = cta.get("booking_btn", "Đặt chuyến đi ngay")
careers_btn_text = cta.get("careers_btn", "Gia nhập đội ngũ")

html_cta = f"""
<section class="team-cta">
    <div class="team-page-wrap team-cta-inner">
        <span class="team-eyebrow">{cta_eyebrow}</span>
        <h2>{cta_title}</h2>
        <p>{cta_subtitle}</p>
        <div class="team-cta-buttons">
            <a href="/Booking" class="team-cta-btn primary">{booking_btn_text}</a>
            <a href="/Careers" class="team-cta-btn secondary">{careers_btn_text}</a>
        </div>
    </div>
</section>
"""
st.markdown(html_cta, unsafe_allow_html=True)


# ── Footer ──────────────────────────────────────────────────────────────────────
render_footer()
render_chat_widget()