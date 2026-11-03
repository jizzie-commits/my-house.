import streamlit as st
import math

# 1. 페이지 기본 설정
st.set_page_config(page_title="Tiny Haven - 귀여운 아지트 집짓기", page_icon="🏠", layout="wide", initial_sidebar_state="expanded")

# 2. 파스텔 스타일 CSS
custom_css = "<style>@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap'); html, body, [class*='css'] { font-family: 'Nanum Gothic', sans-serif; } h1, h2, h3 { font-family: 'Jua', sans-serif !important; color: #FF6B81 !important; } .stApp { background-color: #FFF9F5; } .house-card { background: linear-gradient(135deg, #FFE5EC 0%, #F0E6FF 100%); border: 3px solid #FFB7B2; border-radius: 20px; padding: 25px; box-shadow: 0 10px 20px rgba(255, 183, 178, 0.3); margin-bottom: 25px; } .badge { background-color: #FF8E9E; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.85rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 10px; } .house-title { font-family: 'Jua', sans-serif; font-size: 2rem; color: #4A4E69; margin-top: 5px; margin-bottom: 15px; } .info-box { background-color: #E8F8F5; border-left: 5px solid #2ECC71; padding: 12px 15px; border-radius: 8px; font-size: 0.95rem; color: #27AE60; margin-top: 10px; }</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# 3. 타이틀
st.title("🏡 Tiny Haven : 세상에서 가장 귀여운 나만의 아지트")
st.caption("당신의 공간 취향과 대지의 기후·지형을 분석해 꼭 맞는 동화 속 작은 집을 지어드려요! ✨")
st.divider()

# 4. 사이드바 입력창
with st.sidebar:
    st.header("🎨 1. 나만의 취향 선택하기")
    purpose = st.selectbox("아지트의 주 용도는 무엇인가요?", ["🍵 따스한 티하우스 & 독서실", "🎨 몽상가의 그림 아뜰리에", "🌲 숲속 힐링 휴식처", "🏕️ 오프그리드 모험 캐빈"])
    mood = st.radio("선호하는 공간 분위기는?", ["아늑하고 감싸주는 비밀 기지 (내향형)", "햇살 가득 창이 넓은 개방형 (외향형)"], index=1)
    color_theme = st.selectbox("좋아하는 건축 포인트 컬러", ["🌸 파스텔 피치 핑크", "🌿 숲속 메론 그린", "🌼 포근한 크림 옐로우", "🫐 은은한 라벤더 블루"])
    
    st.divider()
    st.header("🌍 2. 대지 기후 및 지형 입력")
    snow = st.number_input("🌨️ 연중 최대 적설량 (cm)", min_value=0.0, max_value=300.0, value=15.0, step=5.0)
    wind = st.number_input("💨 최대 예상 풍속 (m/s)", min_value=0.0, max_value=80.0, value=12.0, step=1.0)
    slope = st.slider("⛰️ 대지 경사도 (°)", min_value=0, max_value=45, value=5)
    sunlight = st.slider("☀️ 일일 평균 일조시간 (시간)", min_value=1.0, max_value=15.0, value=6.0, step=0.5)
    area = st.number_input("📐 아지트 크기 (평)", min_value=3.0, max_value=15.0, value=6.0, step=0.5)

# 5. 건축 조건 산출 알고리즘
if snow >= 50:
    roof_style = "뾰족한 동화 속 과자집 지붕 (급경사 박공 45°)"
    roof_desc = "눈이 스르륵 미끄러져 쌓이지 않는 안전하고 귀여운 세모 지붕이에요!"
    house_type_name = "눈송이 살구집 ❄️"
elif snow >= 20:
    roof_style = "아늑한 버섯 모양 삼각 지붕 (완경사 30°)"
    roof_desc = "비와 눈이 잘 흘러내리는 둥글둥글 안락한 지붕이에요."
    house_type_name = "도토리 다락집 🌰"
else:
    roof_style = "평평한 옥상 테라스 지붕 (10°)"
    roof_desc = "햇살을 받으며 음료를 마실 수 있는 예쁜 옥상 공간이 생겨요!"
    house_type_name = "햇살 햇빛 상자 ☀️"

if slope >= 15:
    foundation_style = "동화 속 새둥지 다리 구조 (고상식 파일 기초)"
    foundation_desc = "경사지를 깎지 않고 나무 기둥 위에 아지트를 살포시 올려 자연을 보존해요."
else:
    foundation_style = "탄탄하고 포근한 매트 기초"
    foundation_desc = "평평하고 안정감 있게 땅에 쏙 들어앉은 구조예요."

if wind >= 25:
    wall_style = "단단한 탄화목 & 로즈골드 내후성 스틸"
    wall_desc = "강한 바람도 거뜬히 막아주는 튼튼하고 근사한 외벽이에요."
else:
    wall_style = "따스한 파스텔 원목 슬릿 & 내추럴 우드"
    wall_desc = "자연 친화적이고 아기자기한 목조 질감을 살렸어요."

if "내향형" in mood:
    window_style = "아늑한 동그라미 아치창 & 코너 액자창"
    window_desc = "외부 시선은 차단하면서 나만의 차분한 조명을 연출해 줘요."
else:
    window_style = "3면 파노라마 통유리 & 아치형 천장창"
    window_desc = "바깥 풍경이 한눈에 들어오고 햇살이 온몸을 감싸줘요."

solar_panels = math.ceil((area * 1.5) / max(sunlight, 1.0))

# 6. 메인 결과 레이아웃
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("🎀 완성된 나만의 맞춤 아지트 컨셉")
    bp = purpose.split()[1] if len(purpose.split()) > 1 else purpose
    bc = color_theme.split()[1] if len(color_theme.split()) > 1 else color_theme
    
    card_html = f'<div class="house-card"><span class="badge">{bp}</span><span class="badge">{bc}</span><div class="house-title">✨ {house_type_name}</div><p><b>📐 아지트 규모:</b> 전용 {area}평형 소형 건축물</p><p><b>🏠 추천 지붕:</b> {roof_style}<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>└ {roof_desc}</i></p><p><b>🧱 외벽 & 구조:</b> {wall_style}<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>└ {wall_desc}</i></p><p><b>🪜 대지 기초:</b> {foundation_style}<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>└ {foundation_desc}</i></p><p><b>🪟 창호 디자인:</b> {window_style}<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>└ {window_desc}</i></p></div>'
    st.markdown(card_html, unsafe_allow_html=True)

with col2:
    st.subheader("⚡ 자립형 미니 에너지 계산기")
    st.metric(label="💡 하루 필요한 친환경 태양광 패널", value=f"{solar_panels} 개")
    st.caption(f"기준: 하루 평균 {sunlight}시간 일조량 및 {area}평 공간 사용 시")
    
    info_html = '<div class="info-box"><b>🌱 친환경 오프그리드 Tip:</b><br>소형 빗물 수집 장치와 미니 태양광 패널만으로도 작은 티하우스의 전등과 스피커를 충분히 작동시킬 수 있어요!</div>'
    st.markdown(info_html, unsafe_allow_html=True)

# 7. 사양 요약 표
st.divider()
st.subheader("📋 건축 사양 요약 리포트")
report_data = {
    "항목": ["건축물 명칭", "용도", "건축 면적", "지붕 형태", "기초 방식", "창호 스펙", "필요 태양광 패널"],
    "설계 사양": [house_type_name, purpose, f"{area} 평", roof_style, foundation_style, window_style, f"{solar_panels} 개"],
    "적용 환경 원인": ["기후/지형/취향 종합", "사용자 선택", "사용자 선택", f"적설량 {snow}cm 반영", f"경사도 {slope}° 반영", mood, f"일조시간 {sunlight}시간 반영"]
}
st.table(report_data)
st.success("🎉 성공적으로 나만의 귀여운 아지트 설계가 완료되었습니다!")
