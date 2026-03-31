import base64
import os
import streamlit as st

# Đoạn mã này để nạp Font Awesome vào website
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

def load_css(path):
    """Đọc file CSS và tiêm vào Streamlit"""
    # Điều chỉnh đường dẫn linh hoạt
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_optimized_url(url, width=800, quality=75):
    """
    Tự động thêm tham số nén ảnh cho Unsplash
    """
    if "images.unsplash.com" in url:
        base_url = url.split('?')[0]
        return f"{base_url}?auto=format&fit=crop&q={quality}&w={width}&fm=webp"
    return url

def load_all_global_css():
    """
    Nạp tất cả các file CSS từ thư mục assets/css/
    để đảm bảo giao diện đồng nhất trên mọi trang.
    """
    css_files = [
        "assets/css/base.css",
        "assets/css/navbar.css",
        "assets/css/hero.css",
        "assets/css/footer.css",
        "assets/css/components.css",
        "assets/css/style.css"
    ]
    
    for css_path in css_files:
        load_css(css_path)

def get_local_img_url(path):
    """Chuyển ảnh local thành base64 để hiển thị trong HTML"""
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        ext = os.path.splitext(path)[1][1:]
        return f"data:image/{ext};base64,{base64.b64encode(data).decode()}"
    return "https://via.placeholder.com/150"