"""
Dán đoạn này vào đầu mỗi file trong pages/ (sau st.set_page_config)
để ẩn navigation tự động và thêm nút Back về trang chủ.
"""
import streamlit as st

def hide_auto_nav():
    st.markdown("""
    <style>
    [data-testid="stSidebarNavItems"],
    [data-testid="stSidebarNavSeparator"],
    [data-testid="collapsedControl"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.page_link("app.py", label="🏠 Trang chủ AIDEOM-VN")
        st.markdown("---")
