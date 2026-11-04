import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 & 세션 상태 관리
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Minecraft Haven - 고퀄리티 3D 집 & 미니 지구본",
    page_icon="🐷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "start"

def reset_app():
    st.session_state.page = "start"

# -----------------------------------------------------------------------------
# 2. 커스텀 CSS 스타일
# -----------------------------------------------------------------------------
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
html, body, [class*='css'] { font-family: 'Jua', sans-serif !important; }
.stApp { background: linear-gradient(180deg, #74b9ff 0%, #a1c4fd 40%, #55efc4 100%); }
.mc-box { background: #576574; border: 4px solid #222f3e; border-radius: 12px; padding: 20px; color: white; box-shadow: 0 6px 0px #222f3e; margin-bottom: 15px; }
.badge { background-color: #ff6b6b; color: white; padding: 4px 10px; border-radius: 6px; font-size: 0.9rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 8px; border: 2px solid #ee5253; }
.title-txt { font-family: 'Jua', sans-serif; font-size: 2rem; color: #fabca1; text-shadow: 2px 2px 0px #000; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# =============================================================================
# [화면 1] 시작 화면
# =============================================================================
if st.session_state.page == "start":
    st.markdown('<div style="text-align:center; padding: 20px 0;"><h1 style="font-size: 3.5rem; color: #fff; text-shadow: 3px 3px 0px #2d3436;">⛏️ MINECRAFT TINY HAVEN 🐷</h1><p style="font-size: 1.3rem; color: #f1f2f6; text-shadow: 1px 1px 0px #000;">귀여운 3D 하트 돼지와 함께 만드는 고퀄리티 마인크래프트 입체 아지트 ✨</p></div>', unsafe_allow_html=True)

    pig_3d_html = """
    <div id="pig-container" style="width:100%; height:300px; border-radius:15px; overflow:hidden; background: transparent;"></div>
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
    st.components.v1.html(pig_3d_html, height=310)

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
    st.caption("원하는 항목을 선택한 후 아래 [🏡 고퀄리티 마인크래프트 집 생성] 버튼을 클릭하세요.")
    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("1. 건축 스타일 및 분위기")
        house_style = st.selectbox("🏰 건물 양식", [
            "모던 럭셔리 수영장 빌라 (Modern Villa)",
            "유럽풍 클래식 판타지 캐빈 (Medieval Cottage)",
            "해안가 럭셔리 리조트 하우스 (Beach Resort)",
            "도심 속 모던 고층 아지트 (City Penthouse)"
        ])
        season = st.selectbox("🌸 사계절 선택", ["봄 (Spring)", "여름 (Summer)", "가을 (Autumn)", "겨울 (Winter)"])

    with col_b:
        st.subheader("2. 날씨 및 블록 재료")
        weather = st.selectbox("🌦️ 원하는 날씨", ["화창한 햇살 맑은 날", "비 내리는 운치 있는 날", "눈 내리는 흰 겨울 날", "노을빛 석양 날"])
        material = st.selectbox("🧱 주요 마인크래프트 블록", [
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
    st.subheader("🐷 하트 돼지가 배경 산과 마인크래프트 집을 디자인하는 중입니다...")
    st.caption("실제 지구본 매칭 및 입체 배경을 구성하고 있습니다 ⏳")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    
    st.session_state.page = "result"
    st.rerun()

# =============================================================================
# [화면 4] 초고퀄리티 3D 집 (배경 포함) & 실제 미니 지구본
# =============================================================================
elif st.session_state.page == "result":
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.title("✨ 완공된 3D 마인크래프트 건축물")
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
        country_name = "미국 캘리포니아 (말리부)"
        country_feature = "태평양 해안선을 따라 형성된 고급 해양 빌라 지구입니다. 온난한 지중해성 기후로 야외 수영장과 시원한 유리 통창 구조가 특징입니다."
        lat, lon = 34.0259, -118.7798
        b_color, r_color, s_color = "0xeaeaea", "0x2c3e50", "0x00a8ff"
    elif "유럽풍" in house_style:
        country_name = "독일 바이에른 (알프스 산간 마을)"
        country_feature = "유럽 전통 목조 아치 구조와 울창한 숲이 어우러진 차분한 동화 마을입니다. 눈과 비에 강한 경사 박공지붕과 포근한 목재 질감이 매력적입니다."
        lat, lon = 47.5596, 10.7498
        b_color, r_color, s_color = "0x8d5b4c", "0xa93226", "0x27ae60"
    elif "해안가" in house_style:
        country_name = "몰디브 (마벨레 아일랜드)"
        country_feature = "에메랄드빛 해상 위에 지어진 휴양 리조트입니다. 습기와 해풍에 강한 모듈러 데크와 투명한 수평선 뷰를 갖추고 있습니다."
        lat, lon = 3.2028, 73.2207
        b_color, r_color, s_color = "0xf5efff", "0xd35400", "0x00d2d3"
    else:
        country_name = "아랍에미리트 두바이 (초고층 도심)"
        country_feature = "미래지향적 도심 경관과 화려한 석양이 어우러지는 현대식 스카이라인입니다. 내후성이 강한 스틸 자재와 옥상 라운지가 배치됩니다."
        lat, lon = 25.2048, 55.2708
        b_color, r_color, s_color = "0x7f8c8d", "0x16a085", "0xf1c40f"

    # 1. 자연 배경(산, 언덕, 대지)이 포함된 3D 마인크래프트 집 HTML
    high_qual_house_template = """
    <div id="mc-container" style="width:100%; height:520px; border-radius:15px; overflow:hidden; background:#81ecec;"></div>
    <script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
    <script>
      const container = document.getElementById('mc-container');
      const scene = new THREE.Scene();
      scene.background = new THREE.Color(0x74b9ff); // 푸른 하늘 배경

      const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(renderer.domElement);

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.85);
      scene.add(ambientLight);
      const dirLight1 = new THREE.DirectionalLight(0xfffaed, 1.3);
      dirLight1.position.set(12, 22, 15);
      scene.add(dirLight1);

      const mainGroup = new THREE.Group();

      // [배경 배경요소] 마인크래프트 잔디 지형 & 뒷산
      const groundMat = new THREE.MeshStandardMaterial({ color: 0x55efc4, roughness: 0.8 });
      const ground = new THREE.Mesh(new THREE.BoxGeometry(14, 0.4, 14), groundMat);
      ground.position.y = -0.2;
      mainGroup.add(ground);

      const mountainMat = new THREE.MeshStandardMaterial({ color: 0x00b894, roughness: 0.9 });
      for (let i = 0; i < 5; i++) {
        const hill = new THREE.Mesh(new THREE.BoxGeometry(3 + i, 2 + i*0.5, 3 + i), mountainMat);
        hill.position.set(-4 + (i*1.5), 0.8 + (i*0.2), -4 - (i*0.5));
        mainGroup.add(hill);
      }

      // [건축물] 디테일한 집 구조
      const houseGroup = new THREE.Group();

      const b1Mat = new THREE.MeshStandardMaterial({ color: __B_COLOR__, roughness: 0.3 });
      const b1 = new THREE.Mesh(new THREE.BoxGeometry(3.4, 1.3, 2.8), b1Mat);
      b1.position.y = 0.65;
      houseGroup.add(b1);

      const b2Mat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.2 });
      const b2 = new THREE.Mesh(new THREE.BoxGeometry(2.5, 1.2, 2.4), b2Mat);
      b2.position.set(-0.35, 1.9, 0.1);
      houseGroup.add(b2);

      const roofMat = new THREE.MeshStandardMaterial({ color: __R_COLOR__ });
      const roof = new THREE.Mesh(new THREE.BoxGeometry(2.7, 0.15, 2.5), roofMat);
      roof.position.set(-0.35, 2.55, 0.1);
      houseGroup.add(roof);

      const winMat = new THREE.MeshStandardMaterial({ color: 0x81ecec, transparent: true, opacity: 0.75, metalness: 0.8 });
      const win1 = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.8, 0.05), winMat);
      win1.position.set(0.6, 0.65, 1.41);
      houseGroup.add(win1);

      const win2 = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.75, 0.05), winMat);
      win2.position.set(-0.35, 1.9, 1.31);
      houseGroup.add(win2);

      const poolMat = new THREE.MeshStandardMaterial({ color: __S_COLOR__, roughness: 0.1, metalness: 0.6 });
      const pool = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.18, 1.8), poolMat);
      pool.position.set(1.3, 0.09, -0.2);
      houseGroup.add(pool);

      mainGroup.add(houseGroup);
      scene.add(mainGroup);

      camera.position.set(7, 5, 8);
      camera.lookAt(0, 1, 0);

      function animate() {
        requestAnimationFrame(animate);
        mainGroup.rotation.y += 0.005;
        renderer.render(scene, camera);
      }
      animate();
    </script>
    """
    high_qual_house_html = high_qual_house_template.replace("__B_COLOR__", str(b_color)).replace("__R_COLOR__", str(r_color)).replace("__S_COLOR__", str(s_color))

    # 2. 실제 지구본 형태(대륙 파랑/초록 텍스처 느낌) 3D 미니 지구본 HTML
    mini_globe_template = """
    <div id="mini-globe-container" style="width:100%; height:180px; border-radius:12px; overflow:hidden; background:#0c2461;"></div>
    <script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
    <script>
      const container = document.getElementById('mini-globe-container');
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(40, container.clientWidth / container.clientHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(renderer.domElement);

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.95);
      scene.add(ambientLight);
      const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
      dirLight.position.set(5, 5, 5);
      scene.add(dirLight);

      const globeGroup = new THREE.Group();

      // 바다 구체 (실제 지구 바다 파란색)
      const oceanGeo = new THREE.SphereGeometry(1.2, 32, 32);
      const oceanMat = new THREE.MeshStandardMaterial({ color: 0x0984e3, roughness: 0.4 });
      const ocean = new THREE.Mesh(oceanGeo, oceanMat);
      globeGroup.add(ocean);

      // 실제 대륙 느낌의 블록형 녹색/갈색 대륙 레이어
      const landGroup = new THREE.Group();
      const landMat = new THREE.MeshStandardMaterial({ color: 0x2ed573, roughness: 0.8 });
      for(let i=0; i<30; i++) {
        const landBlock = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.2, 0.1), landMat);
        const latR = (Math.random() - 0.5) * Math.PI;
        const lonR = (Math.random() - 0.5) * Math.PI * 2;
        landBlock.position.set(1.21 * Math.cos(latR) * Math.cos(lonR), 1.21 * Math.sin(latR), 1.21 * Math.cos(latR) * Math.sin(lonR));
        landGroup.add(landBlock);
      }
      globeGroup.add(landGroup);

      function latLonToVector3(lat, lon, radius) {
        const phi = (90 - lat) * (Math.PI / 180);
        const theta = (lon + 180) * (Math.PI / 180);
        const x = -(radius * Math.sin(phi) * Math.cos(theta));
        const z = (radius * Math.sin(phi) * Math.sin(theta));
        const y = (radius * Math.cos(phi));
        return new THREE.Vector3(x, y, z);
      }

      // 위치 표시 빨간색 3D 화살표
      const markerPos = latLonToVector3(__LAT__, __LON__, 1.25);
      const arrowGroup = new THREE.Group();
      const cone = new THREE.Mesh(new THREE.ConeGeometry(0.12, 0.28, 12), new THREE.MeshStandardMaterial({ color: 0xff4757, emissive: 0xff6b81, emissiveIntensity: 0.8 }));
      cone.rotation.x = Math.PI;
      arrowGroup.add(cone);

      arrowGroup.position.copy(markerPos);
      arrowGroup.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), markerPos.clone().normalize());

      globeGroup.add(arrowGroup);
      scene.add(globeGroup);

      camera.position.set(0, 0, 3.4);

      const targetPos = latLonToVector3(__LAT__, __LON__, 1.2);
      globeGroup.quaternion.setFromUnitVectors(targetPos.clone().normalize(), new THREE.Vector3(0, 0, 1));

      function animate() {
        requestAnimationFrame(animate);
        globeGroup.rotation.y += 0.006;
        renderer.render(scene, camera);
      }
      animate();
    </script>
    """
    mini_globe_html = mini_globe_template.replace("__LAT__", str(lat)).replace("__LON__", str(lon))

    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader("🧊 자연 배경이 포함된 3D 마인크래프트 집")
        st.components.v1.html(high_qual_house_html, height=530)

    with col2:
        st.subheader("🌐 실제 지구본 위치 표시")
        st.components.v1.html(mini_globe_html, height=190)
        
        st.markdown(f"""
        <div class="mc-box">
            <span class="badge">{house_style.split()[0]}</span>
            <span class="badge">{season.split()[0]}</span>
            <div class="title-txt">📍 국가: {country_name}</div>
            <p style="margin-top: 12px; line-height: 1.6; font-size: 1.05rem;">
                <b>🌍 실제 지형 및 기후 특징:</b><br>{country_feature}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📋 건축 사양 리포트")
    report_data = {
        "항목": ["건축 양식", "선택 계절", "선택 날씨", "메인 블록", "매칭 국가 위치"],
        "상세 설명": [house_style, season, weather, material, country_name]
    }
    st.table(report_data)
    st.success("🎉 하트 돼지와 함께한 고퀄리티 마인크래프트 아지트 생성이 완료되었습니다!")
