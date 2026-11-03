import streamlit as st
import math

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 아기자기한 파스텔 CSS 스타일 적용
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Tiny Haven - 귀여운 아지트 집짓기",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 귀여운 파스텔 톤 및 카드 커스텀 스타일링
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Nanum Gothic', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Jua', sans-serif !important;
        color: #FF6B81 !important;
    }
    
    /* 배경 및 서브 카드 디자인 */
    .stApp {
        background-color: #FFF9F5;
    }
    
    /* 귀여운 아지트 결과 카드 */
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
    
    /* 안내 박스 스타일 */
    .info-box {
        background-color: #E8F8F5;
        border-left: 5px solid #2ECC71;
        padding: 12px 15px;
        border-radius: 8px;
        font-size: 0.
