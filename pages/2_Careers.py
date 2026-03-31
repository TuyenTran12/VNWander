import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from utils.helpers import load_all_global_css
from utils.session_init import init_session_state
from config.languages import CONTENT

def main():
    # 1. Khởi tạo
    st.set_page_config(page_title="VNWander - Careers", layout="wide")
    init_session_state()    
    load_all_global_css()
    render_navbar(current_page_path="/Careers")

    if "lang" in st.query_params:
        st.session_state.lang = st.query_params["lang"]
    elif 'lang' not in st.session_state:
        st.session_state.lang = 'vi' 
    # 2. Lấy dữ liệu
    lang = st.session_state.get('lang', 'vi')
    C = CONTENT[lang].get('career_page', {})
    values = C.get('core_values', [])

    # 3. SECTION 1: VĂN HÓA ĐỜI SỐNG (Xếp sát lề để tránh hiện code)
    # Cập nhật nội dung văn bản đầy đủ và thụt lề code Python chuẩn
    st.markdown(f"""
<div style="max-width: 1200px; margin: 0 auto; padding: 60px 20px; display: flex; align-items: center; gap: 60px; flex-wrap: wrap;">
<div style="flex: 1; min-width: 350px;">
<h1 style="font-family: 'Playfair Display', serif; font-size: 3.8rem; color: #4CB5F9; margin-bottom: 25px; font-weight: 800;">
{C.get('culture_title', '')}
</h1>
<p style="font-size: 1.15rem; line-height: 1.8; color: #333; text-align: justify; margin-bottom: 35px;">
Tại VNWander, sứ mệnh của chúng tôi là kiến tạo những sản phẩm tiên phong, nơi mọi giới hạn đều bị xóa nhòa để nhường chỗ cho tinh thần sáng tạo bứt phá. Chúng tôi không chỉ khuyến khích bạn vượt qua những rào cản thông thường mà còn trân trọng từng ý tưởng táo bạo nhất.<br><br>
Nhịp sống mỗi ngày tại đây là sự vận động không ngừng của thị trường và khát khao chinh phục những đỉnh cao mới. Thời gian tại VNWander không gói gọn trong quy định 8 tiếng khô khan; đó là hành trình của những trải nghiệm rực rỡ, nơi bạn thỏa sức sống với đam mê tuổi trẻ, học hỏi miễn phí từ các 'cao nhân' và tận hưởng những giây phút 'chill' hết mình cùng đồng đội.<br><br>
Đề cao sự minh bạch và tôn trọng bản sắc cá nhân, chúng tôi tin rằng sự khác biệt chính là sức mạnh để cùng nhau phát triển. VNWander là một cộng đồng đa sắc màu, luôn sẵn sàng mở rộng vòng tay chào đón những tài năng mới gia nhập hành trình đầy cảm hứng này.
</p>
<button style="background: #111; color: white; padding: 16px 40px; border: none; border-radius: 50px; font-weight: 700; cursor: pointer;">
{C.get('join_btn', 'Join Us')}
</button>
</div>
<div style="flex: 1; min-width: 350px;">
<img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800" style="width: 100%; border-radius: 25px; box-shadow: 0 25px 50px rgba(0,0,0,0.12);">
</div>
</div>
""", unsafe_allow_html=True)

    # 4. SECTION 2: GIÁ TRỊ CỐT LÕI (DRAGGABLE GRID NỀN ĐEN)
    values_html = f"""
<div class="values-dark-section">
<h2 class="values-title-center">{C.get('values_title', 'Giá trị cốt lõi')}</h2>
<div class="values-drag-container">
"""
    # Vòng lặp tạo 8 Card ngang
    for val in values:
        values_html += f"""
<div class="value-card-landscape">
<img src="{val['img']}" alt="{val['title']}">
<div class="value-card-info">
<h4>{val['title']}</h4>
<p style="font-size: 0.9rem; opacity: 0.8; margin: 0;">{val['desc']}</p>
</div>
</div>
"""
    
    # Đóng các thẻ div
    values_html += """
</div>
<p style="text-align: center; color: #555; margin-top: 20px; font-size: 0.9rem; font-style: italic;">(Dùng chuột kéo sang trái/phải để khám phá)</p>
</div>
"""
    st.markdown(values_html, unsafe_allow_html=True)

    # 5. Footer
    render_footer()

if __name__ == "__main__":
    main()