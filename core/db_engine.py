import pyodbc
import pandas as pd
import streamlit as st

# Sử dụng @st.cache_resource để Streamlit chỉ kết nối DB 1 lần duy nhất, giúp web chạy cực nhanh
@st.cache_resource
def init_connection():
    try:
        # Chuỗi kết nối dựa trên thông số máy tính của Leo
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-0INB54K\\SQLEXPRESS;"
            "DATABASE=vn_wander;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        st.error(f"Lỗi kết nối Database: {e}")
        return None

# Hàm lấy dữ liệu từ SQL và chuyển thành bảng Pandas (dễ hiển thị lên web)
@st.cache_data(ttl=600) # Cache dữ liệu 10 phút để giảm tải cho DB
def run_query(query):
    conn = init_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn)
            return df
        except Exception as e:
            st.error(f"Lỗi truy vấn: {e}")
            return None
    return None