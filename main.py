import streamlit as st
import math

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Tiny Haven - 귀여운 아지트 집짓기",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. 아기자기한 파스텔 CSS 스타일 적용 (SyntaxError 방지 처리)
# -----------------------------------------------------------------------------
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Nanum Gothic', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Jua', sans-serif !important;
        color: #FF6B81 !important;
    }
    
    .stApp {
        background-color: #FFF9F5;
    }
    
    .house-card {
        background: linear-gradient(135deg, #FFE5EC 0%, #F0E6FF 100%);
        border: 3px solid #FFB7B2;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 20px rgba(255, 183, 178, 0.3);
        margin-bottom: 25px;
    }
    
    .badge {
        background-color: #FF8E9E;
        color: white;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
        margin-right: 5px;
        margin-bottom: 10px;
    }
    
    .house-title {
        font-family: 'Jua', sans-serif;
        font-size: 2rem;
        color: #4A4E69;
        margin-top: 5px;
        margin-bottom: 15px;
    }
    
    .info-box {
        background-color: #E8F8F5;
        border-left: 5px solid #2ECC71;
        padding: 12px 15px;
        border-radius: 8px;
        font-size: 0.95rem;
        color: #27AE60;
        margin-top: 10px;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. 메인 타이틀 및 소개
# -----------------------------------------------------------------------------
st.title("🏡 Tiny Haven : 세상에서 가장 귀여운 나만의 아지트")
st.caption("당신의 공간 취향과 대지의 기후·지형을 분석해 꼭 맞는 동화 속 작은 집을 지어드려요! ✨")
st.divider()

# -----------------------------------------------------------------------------
# 4. 사이드바 - 사용자 취향 및 환경 데이터 입력
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("🎨 1. 나만의 취향 선택하기")
    
    purpose = st.selectbox(
        "아지트의 주
