import streamlit as st
from components.ai_widget import render_chat_widget
from components.navbar import render_navbar
from components.footer import render_footer
from utils.helpers import load_all_global_css
from utils.session_init import init_session_state
from config.languages import CONTENT

def main():
    # ── Cấu hình trang ──────────────────────────────────────────────
    st.set_page_config(page_title="VNWander - Tuyển dụng", layout="wide")
    init_session_state()
    load_all_global_css()
    
    if "lang" in st.query_params:
        st.session_state.lang = st.query_params["lang"]
    elif 'lang' not in st.session_state:
        st.session_state.lang = 'vi'

    lang = st.session_state.get('lang', 'vi')
    C = CONTENT[lang].get('career_page', {})
    
    render_navbar(current_page_path="/Careers")

    # ── DỮ LIỆU DỰ PHÒNG (Tránh lỗi sập web) ─────────────────────────
    culture_title = C.get('culture_title', 'Văn hóa & Đời sống')
    join_btn = C.get('join_btn', 'Khám phá ngay')
    
    # Dữ liệu mẫu xịn xò nếu dictionary bị trống
    default_perks = [
        {"icon": "✈️", "title": "Travel Credits", "desc": "Ngân sách du lịch hàng năm và giảm giá cực sâu cho gia đình và bạn bè."},
        {"icon": "🌍", "title": "Fam Trips", "desc": "Cơ hội đi khảo sát các điểm đến mới hoàn toàn miễn phí để lấy trải nghiệm."},
        {"icon": "💻", "title": "Flexible Working", "desc": "Chính sách làm việc từ xa (Remote) và giờ giấc linh hoạt cho team Tech."},
        {"icon": "🧘", "title": "Wellness & Health", "desc": "Bảo hiểm sức khỏe cao cấp và các workshop chăm sóc sức khỏe tinh thần."}
    ]
    perks_data = C.get('perks_benefits', {}).get('items', default_perks)

    default_learning = [
        {"step": "01", "icon": "🎓", "title": "Training Programs", "desc": "Tài trợ 100% các khóa học nâng cao nghiệp vụ, công nghệ mới và ngoại ngữ."},
        {"step": "02", "icon": "🚀", "title": "Career Roadmap", "desc": "Lộ trình thăng tiến minh bạch từ Intern, Junior lên Senior và Management."},
        {"step": "03", "icon": "🤝", "title": "Mentorship", "desc": "Chương trình 1-kèm-1 với các chuyên gia đầu ngành trong suốt 6 tháng đầu."}
    ]
    learning_data = C.get('learning_development', {}).get('roadmap_steps', default_learning)

    default_jobs = [
        {"name": "💻 Engineering & Product", "jobs": [
            {"title": "Senior Fullstack Python Developer", "location": "Hà Nội / Remote"},
            {"title": "UX/UI Product Designer", "location": "Hồ Chí Minh"}
        ]},
        {"name": "🌍 Operations & Travel Experts", "jobs": [
            {"title": "Senior Travel Consultant", "location": "Đà Nẵng"},
            {"title": "Local Experience Guide", "location": "Sapa / Hội An"}
        ]},
        {"name": "🚀 Sales & Marketing", "jobs": [
            {"title": "Digital Marketing Manager", "location": "Hà Nội"},
            {"title": "B2B Partnership Executive", "location": "Hồ Chí Minh"}
        ]}
    ]
    jobs_data = C.get('open_positions', {}).get('departments', default_jobs)

    # ── KHỞI TẠO HTML (SINGLE-LINE BẢO MẬT) ──────────────────────────
    html_careers = '<div class="careers-wrapper">'

    # ===== SECTION 1: HERO & CULTURE =====
    html_careers += (
        '<section class="cr-hero-section">'
        '<div class="cr-container cr-hero-flex">'
        '<div class="cr-hero-text">'
        '<span class="cr-eyebrow">CÙNG NHAU KIẾN TẠO</span>'
        f'<h1 class="cr-title">{culture_title}</h1>'
        '<p class="cr-desc">Tại VNWander, sứ mệnh của chúng tôi là kiến tạo những sản phẩm tiên phong, nơi mọi giới hạn đều bị xóa nhòa. Chúng tôi không gói gọn trong quy định 8 tiếng khô khan; đó là hành trình của những trải nghiệm rực rỡ, nơi bạn thỏa sức sống với đam đam mê và khám phá thế giới.</p>'
        f'<a href="#jobs" class="cr-btn-primary">{join_btn} <span class="arrow">→</span></a>'
        '</div>'
        '<div class="cr-hero-image">'
        '<div class="image-blob"></div>'
        '<img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800" alt="VNWander Culture">'
        '</div>'
        '</div>'
        '</section>'
    )

    # ===== SECTION 2: PERKS & BENEFITS (ĐẶC QUYỀN TRẢI NGHIỆM) =====
    html_careers += (
        '<section class="cr-perks-section">'
        '<div class="cr-container">'
        '<div class="cr-section-header">'
        '<span class="cr-eyebrow">ĐÃI NGỘ XỨNG TẦM</span>'
        '<h2 class="cr-title">Đặc quyền dành riêng cho bạn</h2>'
        '<div class="cr-divider"></div>'
        '</div>'
        '<div class="cr-perks-grid">'
    )
    for p in perks_data:
        html_careers += (
            f'<div class="cr-perk-card">'
            f'<div class="cr-perk-icon-wrap"><div class="cr-perk-icon">{p.get("icon", "✨")}</div></div>'
            f'<h3 class="cr-perk-title">{p.get("title", "")}</h3>'
            f'<p class="cr-perk-desc">{p.get("desc", "")}</p>'
            f'</div>'
        )
    html_careers += '</div></div></section>'

    # ===== SECTION 3: LEARNING & DEVELOPMENT (LỘ TRÌNH PHÁT TRIỂN) =====
    html_careers += (
        '<section class="cr-learning-section">'
        '<div class="cr-container">'
        '<div class="cr-section-header">'
        '<span class="cr-eyebrow">KHÔNG NGỪNG TIẾN BƯỚC</span>'
        '<h2 class="cr-title">Phát triển sự nghiệp cùng VNWander</h2>'
        '<div class="cr-divider"></div>'
        '</div>'
        '<div class="cr-roadmap-container">'
    )
    for l in learning_data:
        html_careers += (
            f'<div class="cr-roadmap-step">'
            f'<div class="cr-step-number">{l.get("step", "00")}</div>'
            f'<div class="cr-step-content">'
            f'<div class="cr-step-icon">{l.get("icon", "🎯")}</div>'
            f'<div><h3 class="cr-step-title">{l.get("title", "")}</h3>'
            f'<p class="cr-step-desc">{l.get("desc", "")}</p></div>'
            f'</div></div>'
        )
    html_careers += '</div></div></section>'

    # ===== SECTION 4: OPEN POSITIONS (VỊ TRÍ TUYỂN DỤNG) =====
    html_careers += (
        '<section id="jobs" class="cr-jobs-section">'
        '<div class="cr-container">'
        '<div class="cr-section-header">'
        '<span class="cr-eyebrow">GIA NHẬP ĐỘI NGŨ</span>'
        '<h2 class="cr-title">Các vị trí đang mở</h2>'
        '<div class="cr-divider"></div>'
        '</div>'
        '<div class="cr-jobs-accordion">'
    )
    for dept in jobs_data:
        html_careers += (
            f'<div class="cr-dept-group">'
            f'<h3 class="cr-dept-name">{dept.get("name", "")}</h3>'
            f'<div class="cr-job-list">'
        )
        for job in dept.get('jobs', []):
            html_careers += (
                f'<div class="cr-job-item">'
                f'<div class="cr-job-info">'
                f'<h4 class="cr-job-title">{job.get("title", "")}</h4>'
                f'<span class="cr-job-location"><i class="fas fa-map-marker-alt"></i> 📍 {job.get("location", "")}</span>'
                f'</div>'
                f'<a href="#" class="cr-btn-apply">Apply Now <span class="arrow">→</span></a>'
                f'</div>'
            )
        html_careers += '</div></div>'

    html_careers += '</div></div></section></div>' # Đóng wrapper

    # ── RENDER 1 LẦN DUY NHẤT ───────────────────────────────────────
    st.markdown(html_careers, unsafe_allow_html=True)
    render_footer()
    render_chat_widget()

if __name__ == "__main__":
    main()