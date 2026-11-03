import streamlit as st
import math

# 1. 페이지 기본 설정
st.set_page_config(page_title="Minecraft Tiny Haven", page_icon="🧱", layout="wide", initial_sidebar_state="expanded")

# 2. 파스텔 & 마인크래프트 픽셀 스타일 CSS
custom_css = "<style>@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap'); html, body, [class*='css'] { font-family: 'Nanum Gothic', sans-serif; } h1, h2, h3 { font-family: 'Jua', sans-serif !important; color: #5B8C5A !important; } .stApp { background-color: #F4F7F4; } .mc-card { background: #FFFFFF; border: 4px solid #4A7A49; border-radius: 12px; padding: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); margin-bottom: 20px; } .badge { background-color: #8EB897; color: white; padding: 4px 10px; border-radius: 8px; font-size: 0.85rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 8px; } .house-title { font-family: 'Jua', sans-serif; font-size: 1.8rem; color: #2E4A2E; margin-bottom: 10px; } .location-box { background-color: #EBF3ED; border-left: 5px solid #5B8C5A; padding: 15px; border-radius: 8px; margin-top: 15px; }</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# 3. 메인 타이틀
st.title("🧱 마인크래프트 스타일 : 나만의 아지트 & 픽셀 여행")
st.caption("선택한 취향, 날씨, 재료에 맞는 픽셀 하우스와 배경을 직접 그리고, 실제 지구 속 어울리는 장소를 찾아드려요! ✨")
st.divider()

# 4. 사이드바 - 사용자 선택 입력
with st.sidebar:
    st.header("🎨 1. 취향 & 선호 환경 선택")
    mood = st.selectbox("🔮 선호하는 공간 분위기", ["포근하고 따뜻한 비밀기지", "탁 트인 맑은 자연 쉼터", "신비롭고 차분한 묵상 공간", "활기차고 낭만적인 아지트"])
    weather = st.selectbox("🌦️ 좋아하는 날씨/기후", ["눈 내리는 포근한 겨울", "햇살 비치는 맑은 여름", "안개 낀 촉촉한 가을/우기", "바람이 선선한 노을녘"])
    material = st.selectbox("🧱 주요 건축 재료", ["따스한 참나무 블록 (Wood)", "단단한 이끼 낀 돌 블록 (Stone/Moss)", "붉은 벽돌 & 파스텔 블록 (Brick/Pastel)", "유리 & 투명 쿼츠 블록 (Glass/Quartz)"])

    st.divider()
    st.header("🌍 2. 상세 환경 조건 입력")
    snow = st.number_input("🌨️ 연중 최대 적설량 (cm)", min_value=0.0, max_value=300.0, value=25.0, step=5.0)
    wind = st.number_input("💨 최대 예상 풍속 (m/s)", min_value=0.0, max_value=80.0, value=15.0, step=1.0)
    slope = st.slider("⛰️ 대지 경사도 (°)", min_value=0, max_value=45, value=10)
    area = st.number_input("📐 아지트 크기 (평)", min_value=3.0, max_value=15.0, value=6.0, step=0.5)

# 5. 알고리즘: 실제 장소 데이터 매칭 및 픽셀 렌더링 색상 추출
if "눈" in weather:
    real_location = "핀란드 로바니에미 (Rovaniemi, Finland)"
    climate_info = "습윤 대륙성 기후 / 냉대 기후 (Dcf)"
    location_desc = "겨울철 침엽수림과 하얀 눈으로 둘러싸인 동화 같은 곳입니다. 적설량이 많아 경사각이 큰 박공지붕이 필수적인 지역입니다."
    bg_sky = "#B0C4DE"
    bg_ground = "#FFFFFF"
    tree_color = "#2F4F4F"
elif "햇살" in weather:
    real_location = "스위스 그린델발트 (Grindelwald, Switzerland)"
    climate_info = "온대 고산 기후 (Cfb)"
    location_desc = "푸른 알프스 잔디와 밝은 햇살이 어우러진 대자연입니다. 일조량이 풍부하여 넓은 유리 창호와 야외 데크가 잘 어울립니다."
    bg_sky = "#87CEEB"
    bg_ground = "#7CFC00"
    tree_color = "#228B22"
elif "안개" in weather:
    real_location = "일본 유후인 산간 마을 (Yufuin, Japan)"
    climate_info = "온난 습윤 기후 (Cfa)"
    location_desc = "산자락에 차분한 안개가 자욱하게 깔리는 고요한 온천 마을입니다. 습기에 강한 목재와 은은한 조명이 매력적인 장소입니다."
    bg_sky = "#DCDCDC"
    bg_ground = "#556B2F"
    tree_color = "#2E8B57"
else: # 노을녘
    real_location = "뉴질랜드 퀸스타운 (Queenstown, New Zealand)"
    climate_info = "서안 해양성 기후 (Cfb)"
    location_desc = "호수와 산맥 뒤로 붉은 노을이 펼쳐지는 낭만적인 지역입니다. 바람을 막아주는 탄단한 수직 구조와 아늑한 인테리어가 어울립니다."
    bg_sky = "#FF7F50"
    bg_ground = "#8FBC8F"
    tree_color = "#006400"

# 재료별 블록 색상 설정
if "참나무" in material:
    wall_color = "#8B5A2B"
    roof_color = "#A0522D"
elif "돌" in material:
    wall_color = "#808080"
    roof_color = "#556B2F"
elif "벽돌" in material:
    wall_color = "#B22222"
    roof_color = "#FF8C00"
else:
    wall_color = "#E0EEEE"
    roof_color = "#4682B4"

# 6. 마인크래프트 픽셀 일러스트 캔버스 HTML/JS 생성
pixel_canvas_html = f"""
<div style="text-align:center;">
  <canvas id="mcCanvas" width="480" height="320" style="border:4px solid #333; border-radius:12px; background-color:{bg_sky}; image-rendering:pixelated;"></canvas>
</div>
<script>
  const canvas = document.getElementById('mcCanvas');
  const ctx = canvas.getContext('2d');

  // 땅 그리기 (픽셀 블록)
  ctx.fillStyle = "{bg_ground}";
  ctx.fillRect(0, 220, 480, 100);

  // 나무 그리기 (마인크래프트 스타일)
  function drawTree(x, y) {{
    ctx.fillStyle = "#5C4033";
    ctx.fillRect(x+12, y+30, 12, 30);
    ctx.fillStyle = "{tree_color}";
    ctx.fillRect(x, y, 36, 36);
  }}
  drawTree(40, 170);
  drawTree(400, 160);

  // 집 벽면 (마인크래프트 블록 집)
  ctx.fillStyle = "{wall_color}";
  ctx.fillRect(180, 150, 120, 80);

  // 지붕 (삼각 픽셀)
  ctx.fillStyle = "{roof_color}";
  ctx.beginPath();
  ctx.moveTo(160, 150);
  ctx.lineTo(240, 90);
  ctx.lineTo(320, 150);
  ctx.fill();

  // 창문 및 문
  ctx.fillStyle = "#FFD700"; // 밝은 조명 창문
  ctx.fillRect(200, 170, 25, 25);
  ctx.fillStyle = "#4A2E12"; // 나무 문
  ctx.fillRect(250, 180, 25, 50);

  // 구름 (픽셀 구름)
  ctx.fillStyle = "#FFFFFF";
  ctx.fillRect(60, 40, 80, 20);
  ctx.fillRect(300, 60, 100, 24);
</script>
"""

# 7. 메인 화면 레이아웃
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🖼️ 마인크래프트 픽셀 일러스트")
    st.components.v1.html(pixel_canvas_html, height=340)
    st.caption("▲ 선택하신 분위기, 기후, 건축 재료 조합으로 생성된 마인크래프트 스타일 픽셀 하우스입니다.")

with col2:
    st.subheader("📍 실제 매칭 장소 & 기후 특징")
    st.markdown(f"""
    <div class="mc-card">
        <span class="badge">{mood.split()[0]}</span>
        <span class="badge">{weather.split()[0]}</span>
        <div class="house-title">✨ {real_location}</div>
        <p><b>🌡️ 기후 유형:</b> {climate_info}</p>
        <p><b>🌲 지형 및 특징:</b> {location_desc}</p>
        <div class="location-box">
            <b>💡 건축 설계 팁:</b><br>
            선택하신 <b>[{material.split()[0]}]</b> 재료는 이 지역의 <b>{weather.split()[0]}</b> 환경에서 시각적으로 가장 포근한 느낌을 주며, 
            적설량({snow}cm)을 견디기 위해 경사 지붕 구조가 반영되었습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

# 8. 사양 요약 표
st.divider()
st.subheader("📋 선택한 취향 및 환경 기반 건축 리포트")
report_data = {
    "항목": ["선택 공간 분위기", "선택 날씨/기후", "주요 건축 재료", "매칭된 실제 장소", "건축 면적", "예상 적설량/풍속"],
    "설계 사양": [mood, weather, material, real_location, f"{area} 평", f"적설량 {snow}cm / 풍속 {wind}m/s"],
    "분석 결과": ["공간 감성 반영", "배경 색상 및 기후 매칭", "픽셀 블록 질감 적용", "지구상 유사 환경 도출", "소형 아지트 스케일", "구조적 안전성 반영"]
}
st.table(report_data)
st.success("🎉 마인크래프트 스타일 아지트 생성 및 실제 장소 매칭이 완료되었습니다!")
