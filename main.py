import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 세션 관리
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Minecraft 3D Haven - 고퀄리티 마인크래프트 집",
    page_icon="🧱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "start"

def reset_app():
    st.session_state.page = "start"

# -----------------------------------------------------------------------------
# 2. 커스텀 CSS (단일 행 구성으로 구문 오류 완전 방어)
# -----------------------------------------------------------------------------
custom_css = "<style>@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap'); html, body, [class*='css'] { font-family: 'Nanum Gothic', sans-serif; } h1, h2, h3 { font-family: 'Jua', sans-serif !important; color: #2C3E50 !important; } .stApp { background-color: #F4F6F7; } .start-box { text-align: center; padding: 60px 20px; background: #FFFFFF; border: 3px solid #2ECC71; border-radius: 20px; box-shadow: 0 10px 20px rgba(46, 204, 113, 0.15); margin-top: 40px; } .info-card { background: #FFFFFF; border: 2px solid #E5E8E8; border-radius: 15px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; } .badge { background-color: #2ECC71; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 10px; } .country-title { font-family: 'Jua', sans-serif; font-size: 1.8rem; color: #16A085; margin-bottom: 8px; }</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# =============================================================================
# [화면 1] 시작 화면
# =============================================================================
if st.session_state.page == "start":
    start_html = '<div class="start-box"><h1 style="font-size: 3rem; margin-bottom: 15px;">🧱 Minecraft 3D Haven</h1><p style="font-size: 1.2rem; color: #555;">고퀄리티 마인크래프트 건축물 렌더링과 지구본 위치 네비게이션 시스템 ✨</p></div>'
    st.markdown(start_html, unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 마인크래프트 아지트 설계 시작!", use_container_width=True, type="primary"):
            st.session_state.page = "input"
            st.rerun()

# =============================================================================
# [화면 2] 조건 선택 화면
# =============================================================================
elif st.session_state.page == "input":
    st.title("🎨 건축 스타일 & 위치 조건 선택")
    st.caption("원하는 조건들을 고른 후 아래의 [🏡 고퀄리티 마인크래프트 집 생성] 버튼을 눌러주세요.")
    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("1. 건축 스타일 및 분위기")
        house_style = st.selectbox("🏰 원하는 마인크래프트 건물 형태", [
            "모던 럭셔리 수영장 빌라 (Modern Villa)",
            "유럽풍 클래식 판타지 캐빈 (Medieval Cottage)",
            "해안가 럭셔리 리조트 하우스 (Beach Resort)",
            "도심 속 모던 고층 아지트 (City Penthouse)"
        ])
        season = st.selectbox("🌸 배경 사계절", ["봄 (Spring)", "여름 (Summer)", "가을 (Autumn)", "겨울 (Winter)"])

    with col_b:
        st.subheader("2. 날씨 및 주요 블록 재료")
        weather = st.selectbox("🌦️ 원하는 날씨", ["화창한 햇살 맑은 날", "비 내리는 운치 있는 날", "눈 내리는 흰 겨울 날", "노을빛 석양 날"])
        material = st.selectbox("🧱 메인 마인크래프트 블록", [
            "석영 & 흑요석 & 통유리 (Modern)",
            "가공된 참나무 & 암석 & 집조명 (Classic)",
            "백색 콘크리트 & 야자수목 (Resort)",
            "청색 대리석 & 로즈골드 스틸 (Luxury)"
        ])

    st.divider()
    
    if st.button("🏡 고퀄리티 마인크래프트 집 생성!", type="primary", use_container_width=True):
        st.session_state.house_style = house_style
        st.session_state.season = season
        st.session_state.weather = weather
        st.session_state.material = material
        
        st.session_state.page = "loading"
        st.rerun()

# =============================================================================
# [화면 3] 3초 로딩 애니메이션
# =============================================================================
elif st.session_state.page == "loading":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("🔨 3D 마인크래프트 블록을 조합하고 3D 지구본 위치를 계산 중입니다...")
    st.caption("건물의 디테일한 조명과 유리, 테라스 구조를 정밀 렌더링하고 있습니다 ⏳")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    
    st.session_state.page = "result"
    st.rerun()

# =============================================================================
# [화면 4] 고퀄리티 3D 마인크래프트 집 & 지구본 네비게이션 결과 화면
# =============================================================================
elif st.session_state.page == "result":
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.title("✨ 고퀄리티 3D 마인크래프트 건축물 & 위치 지구본")
    with top_col2:
        st.write("")
        if st.button("🔄 다시하기", type="secondary", use_container_width=True):
            reset_app()
            st.rerun()

    st.divider()

    house_style = st.session_state.house_style
    season = st.session_state.season
    weather = st.session_state.weather
    material = st.session_state.material

    # 스타일별 위치 및 3D 그래픽 파라미터 세팅
    if "모던 럭셔리" in house_style:
        country_name = "미국 (USA) - 캘리포니아 말리부"
        country_feature = "해안가를 끼고 있는 현대적이고 세련된 고급 빌라 단지입니다. 넓은 전면 glass 창과 야외 풀장이 어우러져 뛰어난 조망권을 자랑합니다."
        lat, lon = 34.0259, -118.7798
        b_color, r_color, s_color = "0xeaeaea", "0x2c3e50", "0x00a8ff"
    elif "유럽풍" in house_style:
        country_name = "독일 (Germany) - 바이에른 산간 마을"
        country_feature = "중세 유럽 양식의 아기자기한 삼각 목조 지붕과 돌벽이 어우러진 동화 같은 건축물입니다. 따스한 조명과 원목 블록의 조화가 매력적입니다."
        lat, lon = 47.5596, 10.7498
        b_color, r_color, s_color = "0x8d5b4c", "0xa93226", "0x27ae60"
    elif "해안가" in house_style:
        country_name = "몰디브 (Maldives) - 마벨레 아일랜드"
        country_feature = "에메랄드빛 바다 위에 세워진 프리미엄 해양 리조트입니다. 수영장 테라스와 지상에서 살짝 떠 있는 고상식 모듈러 구조가 적용되었습니다."
        lat, lon = 3.2028, 73.2207
        b_color, r_color, s_color = "0xf5efff", "0xd35400", "0x00d2d3"
    else: # 도심 속
        country_name = "아랍에미리트 (UAE) - 두바이"
        country_feature = "초고층 모던 빌딩과 최첨단 스틸/유리 자재가 결합된 초현대식 아지트입니다. 야경을 감상할 수 있는 화려한 옥상 라운지가 내장되어 있습니다."
        lat, lon = 25.2048, 55.2708
        b_color, r_color, s_color = "0x7f8c8d", "0x16a085", "0xf1c40f"

    # Three.js 고퀄리티 마인크래프트 입체 집 3D HTML/JS Code
    minecraft_3d_html = f"""
    <div id="mc-container" style="width:100%; height:450px; border-radius:15px; overflow:hidden; background:#1e272e;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
      const container = document.getElementById('mc-container');
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
      renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(renderer.domElement);

      // 고급 조명 연출
      const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
      scene.add(ambientLight);
      const dirLight1 = new THREE.DirectionalLight(0xfffaed, 1.2);
      dirLight1.position.set(10, 20, 15);
      scene.add(dirLight1);

      const houseGroup = new THREE.Group();

      // 디테일한 마인크래프트 다층 블록 구조 생성
      // 1층 본체
      const b1Geo = new THREE.BoxGeometry(3, 1.2, 2.5);
      const b1Mat = new THREE.MeshStandardMaterial({{ color: {b_color}, roughness: 0.3 }});
      const b1 = new THREE.Mesh(b1Geo, b1Mat);
      b1.position.y = 0.6;
      houseGroup.add(b1);

      # 2층 본체 (오프셋 배치로 모던한 디테일 표현)
      const b2Geo = new THREE.BoxGeometry(2.2, 1.1, 2.2);
      const b2Mat = new THREE.MeshStandardMaterial({{ color: 0xffffff, roughness: 0.2 }});
      const b2 = new THREE.Mesh(b2Geo, b2Mat);
      b2.position.set(-0.3, 1.75, 0.1);
      houseGroup.add(b2);

      // 프레임 지붕
      const roofGeo = new THREE.BoxGeometry(2.5, 0.2, 2.4);
      const roofMat = new THREE.MeshStandardMaterial({{ color: {r_color} }});
      const roof = new THREE.Mesh(roofGeo, roofMat);
      roof.position.set(-0.3, 2.4, 0.1);
      houseGroup.add(roof);

      // 전면 럭셔리 통유리창 및 개별 픽셀 프레임
      const winMat = new THREE.MeshStandardMaterial({{ color: 0x81ecec, transparent: true, opacity: 0.75, metalness: 0.8 }});
      const win1
