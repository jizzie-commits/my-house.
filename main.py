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
# 2. 커스텀 CSS 스타일링 (SyntaxError 방지 단일 행 구조)
# -----------------------------------------------------------------------------
custom_css = "<style>@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700&display=swap'); html, body, [class*='css'] { font-family: 'Nanum Gothic', sans-serif; } h1, h2, h3 { font-family: 'Jua', sans-serif !important; color: #2C3E50 !important; } .stApp { background-color: #F8F9FA; } .start-box { text-align: center; padding: 60px 20px; background: #FFFFFF; border: 3px solid #3498DB; border-radius: 20px; box-shadow: 0 10px 20px rgba(52, 152, 219, 0.15); margin-top: 40px; } .result-card { background: #FFFFFF; border: 2px solid #E2E8F0; border-radius: 15px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; } .badge { background-color: #3498DB; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 10px; } .location-title { font-family: 'Jua', sans-serif; font-size: 1.8rem; color: #2C3E50; margin-bottom: 8px; }</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# =============================================================================
# [화면 1] 처음 화면 (시작 버튼)
# =============================================================================
if st.session_state.page == "start":
    start_html = '<div class="start-box"><h1 style="font-size: 3rem; margin-bottom: 15px;">🏠 3D Tiny Haven : 입체 아지트 설계</h1><p style="font-size: 1.2rem; color: #555;">사계절과 좋아하는 분위기를 선택하고, 3D 입체 집과 세계 도시를 확인해보세요! ✨</p></div>'
    st.markdown(start_html, unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 나만의 3D 아지트 만들기 시작!", use_container_width=True, type="primary"):
            st.session_state.page = "input"
            st.rerun()

# =============================================================================
# [화면 2] 전체 화면 선택지 입력
# =============================================================================
elif st.session_state.page == "input":
    st.title("🎨 나만의 취향 & 환경 조건 선택")
    st.caption("원하는 조건들을 고른 후 아래의 [🏡 입체 집 짓기] 버튼을 눌러주세요.")
    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("1. 계절 및 날씨 선택")
        season = st.selectbox("🌸 좋아하거나 맞추고 싶은 사계절", ["봄 (Spring)", "여름 (Summer)", "가을 (Autumn)", "겨울 (Winter)"])
        weather = st.selectbox("🌦️ 좋아하는 날씨", ["화창하고 맑은 날", "촉촉하게 비 오는 날", "눈 내리는 하얀 날", "안개 끼고 차분한 날"])

    with col_b:
        st.subheader("2. 중요하게 생각하는 분위기 요소")
        concept = st.selectbox("✨ 중요하게 생각하는 장소 분위기", ["반짝이는 도시의 야경과 야경 뷰", "고요하고 깊은 숲속의 안식처", "파도가 보이는 해변과 탁 트인 바다", "웅장한 산맥과 평화로운 시골"])
        material = st.selectbox("🧱 선호하는 건축 느낌", ["모던한 유리 & 파스텔 스틸", "따스한 원목 & 자연목", "클래식한 붉은 벽돌", "정갈한 돌 & 콘크리트"])

    st.divider()
    
    if st.button("🏡 입체 집 짓기!", type="primary", use_container_width=True):
        st.session_state.season = season
        st.session_state.weather = weather
        st.session_state.concept = concept
        st.session_state.material = material
        
        st.session_state.page = "loading"
        st.rerun()

# =============================================================================
# [화면 3] 3초 로딩 애니메이션
# =============================================================================
elif st.session_state.page == "loading":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("🔨 3D 입체 집과 매칭 도시를 생성 중입니다...")
    st.caption("선택하신 사계절과 분위기 요소를 3D 그래픽 엔진으로 계산하고 있습니다 ⏳")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    
    st.session_state.page = "result"
    st.rerun()

# =============================================================================
# [화면 4] 3D 입체 집 & 실제 도시 결과 화면 (우측 상단 다시하기 버튼)
# =============================================================================
elif st.session_state.page == "result":
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.title("✨ 완공된 3D 입체 아지트 & 도시 추천")
    with top_col2:
        st.write("")
        if st.button("🔄 다시하기", type="secondary", use_container_width=True):
            reset_app()
            st.rerun()

    st.divider()

    season = st.session_state.season
    weather = st.session_state.weather
    concept = st.session_state.concept
    material = st.session_state.material

    # 조건별 실제 장소 및 3D 컬러 매칭 알고리즘
    if "도시" in concept:
        real_country = "일본 (Japan)"
        real_city = "도쿄 (Tokyo)"
        city_desc = "화려하고 반짝이는 도심의 야경과 편리한 인프라가 갖춰진 곳입니다. 도시의 밤풍경을 조망할 수 있는 넓은 통유리 창호가 어울립니다."
        city_img = "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=600"
        house_color = "0x3498db"
        roof_color = "0x2c3e50"
        bg_color = "#1a252f" if ("비" in weather or "안개" in weather) else "#2c3e50"
    elif "숲속" in concept:
        real_country = "캐나다 (Canada)"
        real_city = "휘슬러 (Whistler)"
        city_desc = "울창한 침엽수림과 맑은 공기가 느껴지는 고요한 숲입니다. 외부 자연과 하나가 되는 따뜻한 원목 아지트에 최적입니다."
        city_img = "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600"
        house_color = "0x8e5a2b"
        roof_color = "0x27ae60"
        bg_color = "#27ae60" if ("봄" in season or "여름" in season) else "#d5dbdb"
    elif "바다" in concept:
        real_country = "그리스 (Greece)"
        real_city = "산토리니 (Santorini)"
        city_desc = "탁 트인 맑은 바다와 수평선이 한눈에 보이는 해안 마을입니다. 강한 해풍과 염해에 견디는 화이트 & 블루 톤이 매력적입니다."
        city_img = "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=600"
        house_color = "0xf0f3f4"
        roof_color = "0x2980b9"
        bg_color = "#85c1e9"
    else:
        real_country = "스위스 (Switzerland)"
        real_city = "체르마트 (Zermatt)"
        city_desc = "웅장한 산맥과 평화로운 초원이 어우러진 대자연입니다. 사계절 변화에 유연하게 대응하는 전통 삼각 지붕 구조가 어울립니다."
        city_img = "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?w=600"
        house_color = "0xd35400"
        roof_color = "0x7f8c8d"
        bg_color = "#a3e4d7"

    # Three.js 3D 렌더링 HTML/JS 코드 (파이썬 에러 방지 단일 규격)
    threejs_html = f"""<div id="canvas-container" style="width:100%; height:380px; border-radius:15px; overflow:hidden; background:{bg_color};"></div><script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script><script>const container = document.getElementById('canvas-container'); const scene = new THREE.Scene(); const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000); const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }}); renderer.setSize(container.clientWidth, container.clientHeight); container.appendChild(renderer.domElement); const ambientLight = new THREE.AmbientLight(0xffffff, 0.7); scene.add(ambientLight); const dirLight = new THREE.DirectionalLight(0xffffff, 0.8); dirLight.position.set(5, 10, 7); scene.add(dirLight); const houseGroup = new THREE.Group(); const bodyGeo = new THREE.BoxGeometry(2, 1.5, 2); const bodyMat = new THREE.MeshStandardMaterial({{ color: {house_color} }}); const body = new THREE.Mesh(bodyGeo, bodyMat); body.position.y = 0.75; houseGroup.add(body); const roofGeo = new THREE.ConeGeometry(1.8, 1.2, 4); const roofMat = new THREE.MeshStandardMaterial({{ color: {roof_color} }}); const roof = new THREE.Mesh(roofGeo, roofMat); roof.position.y = 2.1; roof.rotation.y = Math.PI / 4; houseGroup.add(roof); const doorGeo = new THREE.BoxGeometry(0.5, 0.9, 0.1); const doorMat = new THREE.MeshStandardMaterial({{ color: 0x3e2723 }}); const door = new THREE.Mesh(doorGeo, doorMat); door.position.set(0, 0.45, 1.01); houseGroup.add(door); const winGeo = new THREE.BoxGeometry(0.5, 0.5, 0.1); const winMat = new THREE.MeshStandardMaterial({{ color: 0xffeb3b, emissive: 0xffd54f, emissiveIntensity: 0.5 }}); const win = new THREE.Mesh(winGeo, winMat); win.position.set(0.6, 0.9, 1.01); houseGroup.add(win); scene.add(houseGroup); camera.position.set(3.5, 3.5, 5); camera.lookAt(0, 1, 0); function animate() {{ requestAnimationFrame(animate); houseGroup.rotation.y += 0.01; renderer.render(scene, camera); }} animate();</script>"""

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🧊 3D 입체 집 뷰어 (자동 회전)")
        st.components.v1.html(threejs_html, height=400)
        st.caption("▲ Three.js 3D 엔진으로 렌더링된 입체 집입니다. 천천히 360도 회전하며 형태를 보여줍니다.")

    with col2:
        st.subheader("📍 실제 매칭 국가 & 도시")
        card_html = f'<div class="result-card"><span class="badge">{season.split()[0]}</span><span class="badge">{concept.split()[0]}</span><div class="location-title">🌍 {real_country} - {real_city}</div><p><b>🌡️ 도시 기후 및 특징:</b> {city_desc}</p></div>'
        st.markdown(card_html, unsafe_allow_html=True)
        
        st.write("📷 **실제 도시 풍경 사진:**")
        st.image(city_img, caption=f"실제 {real_city}의 풍경", width=380)

    st.divider()
    st.subheader("📋 입력 조건 요약 리포트")
    report_data = {
        "선택 항목": ["선택한 사계절", "좋아하는 날씨", "핵심 분위기 요소", "건축 스타일", "추천 국가 및 도시"],
        "설계 반영 내용": [season, weather, concept, material, f"{real_country} ({real_city})"]
    }
    st.table(report_data)
    st.success("🎉 3D 입체 집 및 실제 도시 매칭이 성공적으로 완료되었습니다!")
