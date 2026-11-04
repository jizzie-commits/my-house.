import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 & 세션 상태 관리
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Minecraft Haven - 3D 하트돼지와 집짓기",
    page_icon="🐷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "start"

def reset_app():
    st.session_state.page = "start"

# -----------------------------------------------------------------------------
# 2. 마인크래프트 공식 비주얼 테마 CSS
# -----------------------------------------------------------------------------
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
html, body, [class*='css'] { font-family: 'Jua', sans-serif !important; }
.stApp { background: linear-gradient(180deg, #74b9ff 0%, #a1c4fd 40%, #55efc4 100%); }
.mc-box { background: #576574; border: 4px solid #222f3e; border-radius: 12px; padding: 25px; color: white; box-shadow: 0 8px 0px #222f3e; margin-bottom: 20px; }
.badge { background-color: #ff6b6b; color: white; padding: 4px 10px; border-radius: 6px; font-size: 0.9rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 8px; border: 2px solid #ee5253; }
.title-txt { font-family: 'Jua', sans-serif; font-size: 2.2rem; color: #fabca1; text-shadow: 2px 2px 0px #000; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# =============================================================================
# [화면 1] 시작 화면 (3D 하트 돼지)
# =============================================================================
if st.session_state.page == "start":
    st.markdown('<div style="text-align:center; padding: 20px 0;"><h1 style="font-size: 3.5rem; color: #fff; text-shadow: 3px 3px 0px #2d3436;">⛏️ MINECRAFT TINY HAVEN 🐷</h1><p style="font-size: 1.3rem; color: #f1f2f6; text-shadow: 1px 1px 0px #000;">사랑스러운 3D 하트 돼지와 함께 나만의 고퀄리티 마인크래프트 아지트를 만들어보세요! ❤️</p></div>', unsafe_allow_html=True)

    pig_3d_html = """
    <div id="pig-container" style="width:100%; height:320px; border-radius:15px; overflow:hidden; background: transparent;"></div>
    <script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
    <script>
      const container = document.getElementById('pig-container');
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(renderer.domElement);

      const light = new THREE.DirectionalLight(0xffffff, 1.1);
      light.position.set(5, 10, 7);
      scene.add(light);
      scene.add(new THREE.AmbientLight(0xffffff, 0.6));

      const pigGroup = new THREE.Group();
      const bodyMat = new THREE.MeshStandardMaterial({ color: 0xffa8a8, roughness: 0.3 });
      const body = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.2, 2), bodyMat);
      body.position.y = 0.8;
      pigGroup.add(body);

      const head = new THREE.Mesh(new THREE.BoxGeometry(1.3, 1.1, 1.1), bodyMat);
      head.position.set(0, 1.3, 1.2);
      pigGroup.add(head);

      const snoutMat = new THREE.MeshStandardMaterial({ color: 0xff7777 });
      const snout = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.4, 0.3), snoutMat);
      snout.position.set(0, 1.15, 1.8);
      pigGroup.add(snout);

      const eyeMat = new THREE.MeshBasicMaterial({ color: 0x000000 });
      const eye1 = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.2, 0.05), eyeMat);
      eye1.position.set(-0.4, 1.4, 1.76);
      const eye2 = eye1.clone();
      eye2.position.set(0.4, 1.4, 1.76);
      pigGroup.add(eye1); 
      pigGroup.add(eye2);

      for (let x of [-0.5, 0.5]) {
        for (let z of [-0.6, 0.6]) {
          const leg = new THREE.Mesh(new THREE.BoxGeometry(0.45, 0.6, 0.45), bodyMat);
          leg.position.set(x, 0.3, z);
          pigGroup.add(leg);
        }
      }

      const heartGroup = new THREE.Group();
      const heartMat = new THREE.MeshStandardMaterial({ color: 0xff3838, emissive: 0xff4d4d, emissiveIntensity: 0.4 });
      for(let i=0; i<4; i++) {
        const hBox1 = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.3, 0.1), heartMat);
        hBox1.position.set((i%2)*0.25 - 0.2, 2.2 + (i*0.25), (Math.floor(i/2))*0.2);
        heartGroup.add(hBox1);
      }
      pigGroup.add(heartGroup);

      scene.add(pigGroup);
      camera.position.set(3, 3, 5);
      camera.lookAt(0, 1, 0);

      function animate() {
        requestAnimationFrame(animate);
        pigGroup.rotation.y += 0.012;
        heartGroup.position.y = Math.sin(Date.now() * 0.004) * 0.15;
        renderer.render(scene, camera);
      }
      animate();
    </script>
    """
    st.components.v1.html(pig_3d_html, height=330)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("💖 하트 돼지와 함께 집짓기 시작!", use_container_width=True, type="primary"):
            st.session_state.page = "input"
            st.rerun()

# =============================================================================
# [화면 2] 조건 선택 화면
# =============================================================================
elif st.session_state.page == "input":
    st.title("🎨 건축 스타일 & 환경 조건 선택")
    st.caption("원하는 조건들을 고른 후 아래의 [🏡 고퀄리티 마인크래프트 집 생성] 버튼을 눌러주세요.")
    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("1. 건축 스타일 및 분위기")
        house_style = st.selectbox("🏰 원하는 건물 스타일", [
            "모던 럭셔리 수영장 빌라 (Modern Villa)",
            "유럽풍 클래식 판타지 캐빈 (Medieval Cottage)",
            "해안가 럭셔리 리조트 하우스 (Beach Resort)",
            "도심 속 모던 고층 아지트 (City Penthouse)"
        ])
        season = st.selectbox("🌸 사계절 선택", ["봄 (Spring)", "여름 (Summer)", "가을 (Autumn)", "겨울 (Winter)"])

    with col_b:
        st.subheader("2. 날씨 및 블록 재료")
        weather = st.selectbox("🌦️ 원하는 날씨", ["화창한 햇살 맑은 날", "비 내리는 운치 있는 날", "눈 내리는 흰 겨울 날", "노을빛 석양 날"])
        material = st.selectbox("🧱 메인 블록 재료", [
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
# [화면 3] 3초 로딩 화면
# =============================================================================
elif st.session_state.page == "loading":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("🐷 하트 돼지가 열심히 마인크래프트 블록을 쌓고 있습니다...")
    st.caption("건물의 디테일과 3D 지구본 위치를 계산하고 있습니다 ⏳")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    
    st.session_state.page = "result"
    st.rerun()

# =============================================================================
# [화면 4] 고퀄 3D 집 & 3D 지구본 결과 화면
# =============================================================================
elif st.session_state.page == "result":
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.title("✨ 완공된 3D 마인크래프트 아지트 & 위치 탐색")
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
    else:
        country_name = "아랍에미리트 (UAE) - 두바이"
        country_feature = "초고층 모던 빌딩과 최첨단 스틸/유리 자재가 결합된 초현대식 아지트입니다. 야경을 감상할 수 있는 화려한 옥상 라운지가 내장되어 있습니다."
        lat, lon = 25.2048, 55.2708
        b_color, r_color, s_color = "0x7f8c8d", "0x16a085", "0xf1c40f"

    # 3D 집 HTML (파이썬 변수 전처리 방식으로 이스케이프 오류 원천 방지)
    minecraft_3d_template = """
    <div id="mc-container" style="width:100%; height:450px; border-radius:15px; overflow:hidden; background:#1e272e;"></div>
    <script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
    <script>
      const container = document.getElementById('mc-container');
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(renderer.domElement);

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
      scene.add(ambientLight);
      const dirLight1 = new THREE.DirectionalLight(0xfffaed, 1.2);
      dirLight1.position.set(10, 20, 15);
      scene.add(dirLight1);

      const houseGroup = new THREE.Group();

      const b1Mat = new THREE.MeshStandardMaterial({ color: __B_COLOR__, roughness: 0.3 });
      const b1 = new THREE.Mesh(new THREE.BoxGeometry(3, 1.2, 2.5), b1Mat);
      b1.position.y = 0.6;
      houseGroup.add(b1);

      const b2Mat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.2 });
      const b2 = new THREE.Mesh(new THREE.BoxGeometry(2.2, 1.1, 2.2), b2Mat);
      b2.position.set(-0.3, 1.75, 0.1);
      houseGroup.add(b2);

      const roofMat = new THREE.MeshStandardMaterial({ color: __R_COLOR__ });
      const roof = new THREE.Mesh(new THREE.BoxGeometry(2.5, 0.2, 2.4), roofMat);
      roof.position.set(-0.3, 2.4, 0.1);
      houseGroup.add(roof);

      const winMat = new THREE.MeshStandardMaterial({ color: 0x81ecec, transparent: true, opacity: 0.75, metalness: 0.8 });
      const win1 = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.7, 0.05), winMat);
      win1.position.set(0.6, 0.6, 1.26);
      houseGroup.add(win1);

      const poolMat = new THREE.MeshStandardMaterial({ color: __S_COLOR__, roughness: 0.1, metalness: 0.5 });
      const pool = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.15, 1.6), poolMat);
      pool.position.set(1.2, 0.08, -0.2);
      houseGroup.add(pool);

      scene.add(houseGroup);
      camera.position.set(5.5, 4.5, 6.5);
      camera.lookAt(0, 1, 0);

      function animate() {
        requestAnimationFrame(animate);
        houseGroup.rotation.y += 0.008;
        renderer.render(scene, camera);
      }
      animate();
    </script>
    """
    minecraft_3d_html = minecraft_3d_template.replace("__B_COLOR__", str(b_color)).replace("__R_COLOR__", str(r_color)).replace("__S_COLOR__", str(s_color))

    # 3D 지구본 HTML
    globe_3d_template = """
    <div id="globe-container" style="width:100%; height:450px; border-radius:15px; overflow:hidden; background:#0c2461;"></div>
    <script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
    <script>
      const container = document.getElementById('globe-container');
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(renderer.domElement);

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
      scene.add(ambientLight);
      const dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
      dirLight.position.set(5, 10, 7);
      scene.add(dirLight);

      const globeGroup = new THREE.Group();

      const globe = new THREE.Mesh(new THREE.SphereGeometry(2, 32, 32), new THREE.MeshStandardMaterial({ color: 0x1e3799, wireframe: true, transparent: true, opacity: 0.6 }));
      globeGroup.add(globe);

      const innerGlobe = new THREE.Mesh(new THREE.SphereGeometry(1.98, 32, 32), new THREE.MeshStandardMaterial({ color: 0x0a3d62 }));
      globeGroup.add(innerGlobe);

      function latLonToVector3(lat, lon, radius) {
        const phi = (90 - lat) * (Math.PI / 180);
        const theta = (lon + 180) * (Math.PI / 180);
        const x = -(radius * Math.sin(phi) * Math.cos(theta));
        const z = (radius * Math.sin(phi) * Math.sin(theta));
        const y = (radius * Math.cos(phi));
        return new THREE.Vector3(x, y, z);
      }

      const markerPos = latLonToVector3(__LAT__, __LON__, 2.05);
      const arrowGroup = new THREE.Group();

      const cone = new THREE.Mesh(new THREE.ConeGeometry(0.18, 0.4, 16), new THREE.MeshStandardMaterial({ color: 0xff3838, emissive: 0xff4d4d, emissiveIntensity: 0.6 }));
      cone.rotation.x = Math.PI;
      arrowGroup.add(cone);

      arrowGroup.position.copy(markerPos);
      arrowGroup.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), markerPos.clone().normalize());

      globeGroup.add(arrowGroup);
      scene.add(globeGroup);

      camera.position.set(0, 0, 5.2);

      const targetPos = latLonToVector3(__LAT__, __LON__, 2.0);
      globeGroup.quaternion.setFromUnitVectors(targetPos.clone().normalize(), new THREE.Vector3(0, 0, 1));

      function animate() {
        requestAnimationFrame(animate);
        globeGroup.rotation.y += 0.005;
        renderer.render(scene, camera);
      }
      animate();
    </script>
    """
    globe_3d_html = globe_3d_template.replace("__LAT__", str(lat)).replace("__LON__", str(lon))

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🧊 고퀄리티 3D 마인크래프트 하우스")
        st.components.v1.html(minecraft_3d_html, height=470)

    with col2:
        st.subheader("🌍 3D 지구본 위치 (빨간색 화살표 마커)")
        st.components.v1.html(globe_3d_html, height=470)

    st.markdown(f"""
    <div class="mc-box">
        <span class="badge">{house_style.split()[0]}</span>
        <span class="badge">{season.split()[0]}</span>
        <div class="title-txt">📍 위치 : {country_name}</div>
        <p style="margin-top: 10px; line-height: 1.6;"><b>🌍 기후 및 특징:</b> {country_feature}</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📋 선택 사양 요약 리포트")
    report_data = {
        "항목": ["건축 스타일", "계절 선택", "날씨 선택", "메인 블록", "매칭 국가 위치"],
        "설계 상세": [house_style, season, weather, material, country_name]
    }
    st.table(report_data)
    st.success("🎉 하트 돼지와 함께한 마인크래프트 집 생성이 완료되었습니다!")
