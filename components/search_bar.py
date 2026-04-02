import streamlit as st
import datetime

def render_search_bar():
    # Danh sách thành phố
    cities = [
        "An Giang", "Ben Tre", "Binh Duong", "Ca Mau", "Can Tho", "Cao Bang", "Con Dao",
        "Da Lat", "Da Nang", "Dong Nai", "Dong Thap", "Ha Giang", "Ha Long", "Hanoi",
        "Ho Chi Minh City", "Hoi An", "Hue", "Moc Chau", "Nha Trang", "Ninh Binh",
        "Phu Quoc", "Phu Yen", "Quy Nhon", "Sapa", "Tay Ninh", "Vung Tau"
    ]

    st.markdown('<div class="premium-search-wrapper">', unsafe_allow_html=True)
    
    # Sử dụng grid (cột) gốc của Streamlit để căn chỉnh nằm ngang hoàn hảo
    col1, col2, col3, col4, col5 = st.columns([2.5, 1.5, 1.5, 1.2, 2])

    with col1:
        st.markdown('<p class="search-label">Destination</p>', unsafe_allow_html=True)
        # Selectbox cho phép gõ để tìm kiếm, chữ đen, không cần gõ tay hoàn toàn
        destination = st.selectbox("City", cities, index=14, label_visibility="collapsed")

    with col2:
        st.markdown('<p class="search-label">Check-in</p>', unsafe_allow_html=True)
        # Bật Lịch (Calendar) siêu xịn của Streamlit
        checkin = st.date_input("Checkin", datetime.date.today(), label_visibility="collapsed")

    with col3:
        st.markdown('<p class="search-label">Check-out</p>', unsafe_allow_html=True)
        checkout = st.date_input("Checkout", datetime.date.today() + datetime.timedelta(days=1), label_visibility="collapsed")

    with col4:
        st.markdown('<p class="search-label">Guests</p>', unsafe_allow_html=True)
        # Ô nhập số có nút cộng/trừ 
        guests = st.number_input("Guests", min_value=1, max_value=20, value=2, step=1, label_visibility="collapsed")

    with col5:
        st.markdown('<p class="search-label">&nbsp;</p>', unsafe_allow_html=True) # Tạo khoảng trống cho cân
        # Nút bấm thiết kế chuẩn
        search_clicked = st.button("SEARCH TRIPS", type="primary", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Logic: Khi bấm nút sẽ lưu dữ liệu và chuyển trang
    if search_clicked:
        st.session_state.search_params = {
            "destination": destination,
            "checkin": checkin.strftime('%Y-%m-%d'),
            "checkout": checkout.strftime('%Y-%m-%d'),
            "guests": guests
        }
        st.switch_page("pages/5_Booking.py")