import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 & 세션 상태(Session State) 관리
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="3D Tiny Haven - 나만의 입체 아지트",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "start"

def reset_app():
    st.session_state.page = "start"

# -----------------------------------------------------------------------------
# 2. 커스텀 CSS 스타일링
# -----------------------------------------------------------------------------
custom_css = """<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Nanum Gothic', sans-serif; }
h1, h2, h3 { font-family: 'Jua', sans-serif !important; color: #2C3E50 !important; }
.stApp { background-color: #F8F9FA; }

/* 시작 화면 박스 */
.start-box {
    text-align: center;
    padding: 60px 20px;
    background: #FFFFFF;
    border: 3px solid #3498DB;
    border-radius: 20px;
    box-shadow: 0 10px 20px rgba(52, 152, 219, 0.15);
    margin-top: 40px;
}

/* 결과 카드 */
.result-card {
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.badge {
    background-color:
