import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 & 세션 상태 관리
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Minecraft Haven - 고퀄리티 마인크래프트 집 생성기",
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
    st.markdown('<div style="text-align:center; padding: 20px 0;"><h1 style="font-size: 3.5rem; color: #fff; text-shadow: 3px 3px 0px #2d3436;">⛏️ MINECRAFT TINY HAVEN 🐷</h1><p style="font-size: 1.3rem; color: #f1f2f6; text-shadow: 1px 1px 0px #000;">체리 하우스, 판타지 캐빈 등 원하는 마인크래프트 아지트를 만들어보세요! ❤️</p></div>', unsafe_allow_html=True)

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
          leg.position.set(x
