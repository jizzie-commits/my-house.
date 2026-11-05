import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 & 세션 상태 관리
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Minecraft Haven - 마인크래프트 집 설계",
    page_icon="🧱",
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

# -----------------------------------------------------------------------------
# 3D 하트 돼지 HTML
# -----------------------------------------------------------------------------
PIG_HTML_TEMPLATE = """
<div id="pig-container" style="width:100%; height:300px; border-radius:15px; overflow:hidden; background: transparent;"></div>
<script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
<script>
  (function() {
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
  })();
</script>
"""

# =============================================================================
# [화면 1] 시작 화면
# =============================================================================
if st.session_state.page == "start":
    st.markdown('<div style="text-align:center; padding: 20px 0;"><h1 style="font-size: 3.5rem; color: #fff; text-shadow: 3px 3px 0px #2d3436;">⛏️ MINECRAFT HAVEN 🐷</h1></div>', unsafe_allow_html=True)
    st.components.v1.html(PIG_HTML_TEMPLATE, height=310)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 나만의 집 짓기 시작!", use_container_width=True, type="primary"):
            st.session_state.page = "input"
            st.rerun()

# =============================================================================
# [화면 2] 입력 조건 화면
# =============================================================================
elif st.session_state.page == "input":
    st.title("🎨 마인크래프트 건축 스타일 선택")
    st.caption("원하시는 건축 스타일과 배경 날씨 요소를 선택해 주세요.")
    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("1. 대표 마인크래프트 건축 양식")
        house_style = st.selectbox("🏰 집 스타일 선택", [
            "🌸 벚꽃 오두막 & 해안 데크 (Cherry House)",
            "🏰 중세 유럽풍 대저택 (Medieval Manor)",
            "🌿 판타지 이끼 지붕 샬레 (Mossy Cottage)",
            "🔮 보라색 탑 마법사의 집 (Wizard Castle)",
            "🌳 숲속 비밀 나무집 (Secret Treehouse)"
        ])
        season = st.selectbox("🌸 사계절 선택", ["봄 (Spring)", "여름 (Summer)", "가을 (Autumn)", "겨울 (Winter)"])

    with col_b:
        st.subheader("2. 날씨 및 주요 블록")
        weather = st.selectbox("🌦️ 배경 날씨", ["화창한 햇살 맑은 날", "비 내리는 운치 있는 날", "눈 내리는 흰 겨울 날", "노을빛 석양 날"])
        material = st.selectbox("🧱 메인 블록 재료", [
            "벚나무 원목 & 분홍 잎사귀 & 부유 데크",
            "가공된 참나무 & 가문비나무 지붕 & 석재 굴뚝",
            "이끼 낀 딥스레이트 & 덩굴 & 암석",
            "보라색 심층암 지붕 & 양털 탑 & 조명",
            "정글 원목 & 덩굴 & 수목 보강재"
        ])

    st.divider()
    
    if st.button("🏡 집 짓기!", type="primary", use_container_width=True):
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
    st.subheader("🔨 입력하신 날씨와 지형에 맞추어 집을 짓고 있습니다...")
    st.caption("선택하신 마당, 바다, 호수 및 집 디테일을 계산하는 중입니다 ⏳")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    
    st.session_state.page = "result"
    st.rerun()

# =============================================================================
# [화면 4] 디테일 3D 집 & 실제 지구본 결과 화면
# =============================================================================
elif st.session_state.page == "result":
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.title("✨ 완성된 3D 마인크래프트 집")
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

    # 스타일 매칭
    if "벚꽃" in house_style:
        country_name = "일본 교토 (사쿠라 해안)"
        country_feature = "해안가 절벽 위 벚나무 지붕과 긴 나무 데크 다리가 바다로 이어지는 낭만적인 집입니다."
        lat, lon = 35.0116, 135.7681
        style_type = "cherry"
    elif "중세" in house_style:
        country_name = "독일 로텐부르크 (중세 마을)"
        country_feature = "석재 마당과 굴뚝, 이중 박공 지붕 및 정원이 어우러진 차분한 저택입니다."
        lat, lon = 49.3779, 10.1789
        style_type = "medieval"
    elif "이끼" in house_style:
        country_name = "영국 코츠월드 (숲속 정원)"
        country_feature = "자연 연못과 덩굴, 이끼 지붕이 숲속 마당과 일치를 이루는 내추럴 샬레입니다."
        lat, lon = 51.8330, -1.8430
        style_type = "mossy"
    elif "보라색" in house_style:
        country_name = "프랑스 몽생미셸 (해상 성)"
        country_feature = "잔잔한 호수 위에 세워진 보라색 첨탑과 화려한 발코니가 돋보이는 성입니다."
        lat, lon = 48.6360, -1.5115
        style_type = "wizard"
    else: # 나무집
        country_name = "인도네시아 발리 (열대우림)"
        country_feature = "거대한 열대 고목 수목 상부에 위치하며 나뭇잎 마당과 덩굴 사다리가 특징입니다."
        lat, lon = -8.5069, 115.2625
        style_type = "treehouse"

    # 날씨 파라미터 매칭 (배경 하늘, 빛, 강수 효과)
    if "노을" in weather:
        bg_sky = "0xff7675"
        light_color = "0xffeaa7"
        weather_type = "sunset"
    elif "비" in weather:
        bg_sky = "0x636e72"
        light_color = "0xb2bec3"
        weather_type = "rain"
    elif "눈" in weather:
        bg_sky = "0xdff9fb"
        light_color = "0xffffff"
        weather_type = "snow"
    else: # 화창한 날
        bg_sky = "0x74b9ff"
        light_color = "0xfffaed"
        weather_type = "clear"

    # 3D 집 & 선택된 날씨/배경 요소 JavaScript
    HOUSE_3D_TEMPLATE = """
    <div id="mc-container" style="width:100%; height:530px; border-radius:15px; overflow:hidden; background:#74b9ff;"></div>
    <script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
    <script>
      (function() {
        const container = document.getElementById('mc-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(__BG_SKY__);

        const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        const ambientLight = new THREE.AmbientLight(0xffffff, 0.85);
        scene.add(ambientLight);
        const dirLight1 = new THREE.DirectionalLight(__LIGHT_COLOR__, 1.3);
        dirLight1.position.set(12, 22, 15);
        scene.add(dirLight1);

        const mainGroup = new THREE.Group();

        // 선택 스타일별 개별 마당/바다/호수/수목 배경 연출
        const style = "__STYLE_TYPE__";

        if (style === "cherry") {
          // 🌸 벚꽃집: 바다 + 백사장 + 해안 데크 다리
          const seaMat = new THREE.MeshStandardMaterial({ color: 0x0984e3, roughness: 0.1 });
          const sea = new THREE.Mesh(new THREE.BoxGeometry(16, 0.3, 16), seaMat);
          sea.position.y = -0.3;
          mainGroup.add(sea);

          const sandMat = new THREE.MeshStandardMaterial({ color: 0xffeaa7 });
          const sand = new THREE.Mesh(new THREE.BoxGeometry(9, 0.4, 9), sandMat);
          sand.position.set(-2, -0.1, -2);
          mainGroup.add(sand);

          // 집 본체 & 벚꽃 지붕
          const houseMat = new THREE.MeshStandardMaterial({ color: 0xffb8c6 });
          const body = new THREE.Mesh(new THREE.BoxGeometry(3.2, 1.8, 2.6), houseMat);
          body.position.set(-2, 1.0, -2);
          mainGroup.add(body);

          const cherryMat = new THREE.MeshStandardMaterial({ color: 0xff77a9, roughness: 0.6 });
          for(let i=0; i<20; i++) {
            const leaf = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.9, 1.2), cherryMat);
            leaf.position.set(-2 + (Math.random()-0.5)*3.2, 2.6 + Math.random()*1.3, -2 + (Math.random()-0.5)*2.8);
            mainGroup.add(leaf);
          }

          // 바다로 연결되는 나무 다리 (Deck Bridge)
          const bridgeMat = new THREE.MeshStandardMaterial({ color: 0x8d5b4c });
          const bridge = new THREE.Mesh(new THREE.BoxGeometry(6.0, 0.2, 1.2), bridgeMat);
          bridge.position.set(2.0, 0.6, -1.0);
          bridge.rotation.y = -0.3;
          mainGroup.add(bridge);

        } else if (style === "medieval") {
          // 🏰 중세 저택: 넓은 돌 마당 + 작은 호수 + 돌 굴뚝
          const groundMat = new THREE.MeshStandardMaterial({ color: 0x55efc4 });
          const ground = new THREE.Mesh(new THREE.BoxGeometry(14, 0.3, 14), groundMat);
          ground.position.y = -0.2;
          mainGroup.add(ground);

          const pondMat = new THREE.MeshStandardMaterial({ color: 0x74b9ff });
          const pond = new THREE.Mesh(new THREE.BoxGeometry(4, 0.35, 3), pondMat);
          pond.position.set(3, -0.15, 3);
          mainGroup.add(pond);

          const stoneMat = new THREE.MeshStandardMaterial({ color: 0x636e72 });
          const b1 = new THREE.Mesh(new THREE.BoxGeometry(3.6, 1.4, 3.0), stoneMat);
          b1.position.y = 0.7;
          mainGroup.add(b1);

          const woodMat = new THREE.MeshStandardMaterial({ color: 0xd7ccc8 });
          const b2 = new THREE.Mesh(new THREE.BoxGeometry(3.0, 1.5, 2.6), woodMat);
          b2.position.set(0, 2.15, 0);
          mainGroup.add(b2);

          const roofMat = new THREE.MeshStandardMaterial({ color: 0x2d3436 });
          const roof = new THREE.Mesh(new THREE.ConeGeometry(2.8, 1.8, 4), roofMat);
          roof.position.y = 3.8;
          roof.rotation.y = Math.PI / 4;
          mainGroup.add(roof);

          const chimney = new THREE.Mesh(new THREE.BoxGeometry(0.6, 2.4, 0.6), stoneMat);
          chimney.position.set(1.2, 2.8, 0.8);
          mainGroup.add(chimney);

        } else if (style === "wizard") {
          // 🔮 마법사의 집: 호수 위 성 + 보라색 뾰족 탑
          const lakeMat = new THREE.MeshStandardMaterial({ color: 0x0984e3, roughness: 0.2 });
          const lake = new THREE.Mesh(new THREE.BoxGeometry(15, 0.3, 15), lakeMat);
          lake.position.y = -0.2;
          mainGroup.add(lake);

          const islandMat = new THREE.MeshStandardMaterial({ color: 0x2ed573 });
          const island = new THREE.Mesh(new THREE.BoxGeometry(7, 0.5, 7), islandMat);
          island.position.y = 0.0;
          mainGroup.add(island);

          const castleMat = new THREE.MeshStandardMaterial({ color: 0xd7ccc8 });
          const mainCastle = new THREE.Mesh(new THREE.BoxGeometry(2.8, 2.4, 2.6), castleMat);
          mainCastle.position.y = 1.45;
          mainGroup.add(mainCastle);

          const tower = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 1.0, 3.2, 8), castleMat);
          tower.position.set(-1.5, 2.0, -1.0);
          mainGroup.add(tower);

          const spireMat = new THREE.MeshStandardMaterial({ color: 0x8e44ad });
          const spire = new THREE.Mesh(new THREE.ConeGeometry(1.1, 2.5, 8), spireMat);
          spire.position.set(-1.5, 4.8, -1.0);
          mainGroup.add(spire);

        } else if (style === "mossy") {
          // 🌿 이끼 샬레: 자연 정원 마당 + 덩굴 연못
          const yardMat = new THREE.MeshStandardMaterial({ color: 0x00b894 });
          const yard = new THREE.Mesh(new THREE.BoxGeometry(14, 0.3, 14), yardMat);
          yard.position.y = -0.2;
          mainGroup.add(yard);

          const bodyMat = new THREE.MeshStandardMaterial({ color: 0x8d5b4c });
          const body = new THREE.Mesh(new THREE.BoxGeometry(3.2, 1.6, 2.6), bodyMat);
          body.position.y = 0.8;
          mainGroup.add(body);

          const mossMat = new THREE.MeshStandardMaterial({ color: 0x27ae60 });
          const roof = new THREE.Mesh(new THREE.ConeGeometry(2.6, 1.6, 4), mossMat);
          roof.position.y = 2.4;
          roof.rotation.y = Math.PI / 4;
          mainGroup.add(roof);

        } else {
          // 🌳 나무집: 울창한 수목 열대우림 마당
          const jungleGround = new THREE.Mesh(new THREE.BoxGeometry(14, 0.3, 14), new THREE.MeshStandardMaterial({ color: 0x00b894 }));
          jungleGround.position.y = -0.2;
          mainGroup.add(jungleGround);

          const trunkMat = new THREE.MeshStandardMaterial({ color: 0x5c4033 });
          const trunk = new THREE.Mesh(new THREE.BoxGeometry(1.8, 4.2, 1.8), trunkMat);
          trunk.position.y = 2.0;
          mainGroup.add(trunk);

          const houseMat = new THREE.MeshStandardMaterial({ color: 0x8d5b4c });
          const cabin = new THREE.Mesh(new THREE.BoxGeometry(2.8, 1.6, 2.6), houseMat);
          cabin.position.set(0, 3.8, 0);
          mainGroup.add(cabin);

          const leafMat = new THREE.MeshStandardMaterial({ color: 0x27ae60 });
          for(let x = -2; x <= 2; x += 1.2) {
            for(let z = -2; z <= 2; z += 1.2) {
              const leaf = new THREE.Mesh(new THREE.BoxGeometry(1.4, 1.2, 1.4), leafMat);
              leaf.position.set(x * 0.8, 4.8 + (Math.random()*0.3), z * 0.8);
              mainGroup.add(leaf);
            }
          }
        }

        mainGroup.add(houseGroup);
        scene.add(mainGroup);

        camera.position.set(8, 6, 9);
        camera.lookAt(0, 1.5, 0);

        function animate() {
          requestAnimationFrame(animate);
          mainGroup.rotation.y += 0.005;
          renderer.render(scene, camera);
        }
        animate();
      })();
    </script>
    """
    house_3d_html = (
        HOUSE_3D_TEMPLATE
        .replace("__BG_SKY__", str(bg_sky))
        .replace("__LIGHT_COLOR__", str(light_color))
        .replace("__STYLE_TYPE__", style_type)
    )

    # 3D 미니 지구본 JavaScript
    GLOBE_3D_TEMPLATE = """
    <div id="mini-globe-container" style="width:100%; height:180px; border-radius:12px; overflow:hidden; background:#0c2461;"></div>
    <script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
    <script>
      (function() {
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

        const oceanMat = new THREE.MeshStandardMaterial({ color: 0x0984e3, roughness: 0.4 });
        const ocean = new THREE.Mesh(new THREE.SphereGeometry(1.2, 32, 32), oceanMat);
        globeGroup.add(ocean);

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
      })();
    </script>
    """
    globe_3d_html = GLOBE_3D_TEMPLATE.replace("__LAT__", str(lat)).replace("__LON__", str(lon))

    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader("🧊 3D 마인크래프트 집 & 환경 배경")
        st.components.v1.html(house_3d_html, height=530)

    with col2:
        st.subheader("🌐 실제 지구본 위치 표시")
        st.components.v1.html(globe_3d_html, height=190)
        
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
    st.success("🎉 하트 돼지와 함께한 마인크래프트 집 생성이 완료되었습니다!")
    
