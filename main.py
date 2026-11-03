import streamlit as st
import math

# 1. 페이지 기본 설정
st.set_page_config(page_title="Tiny Haven - 귀여운 아지트 집짓기", page_icon="🏠", layout="wide", initial_sidebar_state="expanded")

# 2. 아기자기한 파스텔 CSS 스타일 적용
custom_css = """<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Nanum Gothic', sans-serif; }
h1, h2, h3 { font-family: 'Jua', sans-serif !important; color: #FF6B81 !important; }
.stApp { background-color: #FFF9F5; }
.house-card { background: linear-gradient(135deg, #FFE5EC 0%, #F0E6FF 100%); border: 3px solid #FFB7B2; border-radius: 20px; padding: 25px; box-shadow: 0 10px 20px rgba(255, 183, 178, 0.3); margin-bottom: 25px; }
.badge { background-color: #FF8E9E; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.85rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 10px; }
.house-title { font-family: 'Jua', sans-serif; font-size: 2rem; color: #4A4E69; margin-top: 5px; margin-bottom: 15px; }
.info-box { background-color: #E8F8F5; border-left: 5px solid #2ECC71; padding: 12px 15px; border-radius: 8px; font-size: 0.95rem; color: #27AE60; margin-top: 10px; }
</style>"""

st.markdown(custom_css, unsafe_allow_html=True)

# 3. 메인 타이틀
st.title("🏡 Tiny Haven : 세상에서 가장 귀여운 나만의 아지트")
st.caption("당신의 공간 취향과 대지의 기후·지형을 분석해 꼭 맞는 동화 속 작은 집을 지어드려요! ✨")
st.divider()

# 4. 사이드바 - 입력 영역
with st.sidebar:
    st.header("🎨 1. 나만의 취향 선택하기")
    purpose_options = ["🍵 따스한 티하우스 & 독서실", "🎨 몽상가의 그림 아뜰리에", "🌲 숲속 힐링 휴식처", "🏕️ 오프그리드 모험 캐빈"]
    purpose = st.selectbox("아지트의 주 용도는 무엇인가요?", purpose_options)
    
    mood_options = ["아늑하고 감싸주는 비밀 기지 (내향형)", "햇살 가득 창이 넓은 개방형 (외향형)"]
    mood = st.radio("선호하는 공간 분위기는?", mood_options, index=1)
    
    color_options = ["🌸 파스텔 피치 핑크", "🌿 숲속 메론 그린", "🌼 포근한 크림 옐로우", "🫐 은은한 라벤더 블루"]
    color_theme = st.selectbox("좋아하는 건축 포인트 컬러", color_options)
    
    st.divider()
    st.header("🌍 2. 대지 기후 및 지형 입력")
    snow = st.number_input("🌨️ 연중 최대 적설량 (cm)", min_value=0.0, max_value=300.0, value=15.0, step=5.0)
    wind = st.number_input("💨 최대 예상 풍속 (m/s)", min_value=0.0, max_value=80.0, value=12.0, step=1.0)
    slope = st.slider("⛰️ 대지 경사도 (°)", min_value=0, max_value=45, value=5)
    sunlight = st.slider("☀️ 일일 평균 일조시간 (시간)", min_value=1.0, max_value=15.0, value=6.0, step=0.5)
    area = st.number_input("📐 아지트 크기 (평)", min_value
