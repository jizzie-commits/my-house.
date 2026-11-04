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
# 2. 마인크래프트 공식 비주얼 테마 CSS (단일 행 구성으로 에러 완전 방어)
# -----------------------------------------------------------------------------
custom_css = "<style>@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap'); html, body, [class*='css'] { font-family: 'Jua', sans-serif !important; } .stApp { background: linear-gradient(180deg, #74b9ff 0%, #a1c4fd 40%, #55efc4 100%); } .mc-box { background: #576574; border: 4px solid #222f3e; border-radius: 12px; padding: 25px; color: white; box-shadow: 0 8px 0px #222f3e; margin-bottom: 20px; } .mc-button { background-color: #10ac84; color: white; border: 3px solid #01a3a4; border-radius: 8px; padding: 10px 20px; font-size: 1.2rem; cursor: pointer; text-shadow: 1px 1px 0px #000; } .badge { background-color: #ff6b6b; color: white; padding: 4px 10px; border-radius: 6px; font-size: 0.9rem; font-weight: bold; display: inline-block; margin-right: 5px; margin-bottom: 8px; border: 2px solid #ee5253; } .title-txt { font-family: 'Jua', sans-serif; font-size: 2.2rem; color: #fabca1; text-shadow: 2px 2px 0px #000; }</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# =============================================================================
# [화면 1] 마인크래프트 시작 화면 (3D 하트 돼지 등장)
# =============================================================================
if st.session_state.page == "start":
    st.markdown('<div style="text-align:center; padding: 20px 0;"><h1 style="font-size: 3.5rem; color: #fff; text-shadow: 3px 3px 0px #2d3436;">⛏️ MINECRAFT TINY HAVEN 🐷</h1><p style="font-size: 1.3rem; color: #f1f2f6; text-shadow: 1px 1px 0px #000;">사랑스러운 3D 하트 돼지와 함께 나만의 고퀄리티 마인크래프트 아지트를 만들어보세요! ❤️</p></div>', unsafe_allow_html=True)

    # 3D 하트 돼지 HTML/JS (단일 행으로 묶어서 문자열 오류 완벽 방지)
    pig_3d_html = "<div id='pig-container' style='width:100%; height:320px; border-radius:15px; overflow:hidden; background: transparent;'></div><script src='https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'></script><script>const container = document.getElementById('pig-container'); const scene = new THREE.Scene(); const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000); const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true }); renderer.setSize(container.clientWidth, container.clientHeight); container.appendChild(renderer.domElement); const light = new THREE.DirectionalLight(0xffffff, 1.1); light.position.set(5, 10, 7); scene.add(light); scene.add(new THREE.AmbientLight(0xffffff, 0.6)); const pigGroup = new THREE.Group(); const bodyMat = new THREE.MeshStandardMaterial({ color: 0xffa8a8, roughness: 0.3 }); const body = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.2, 2), bodyMat); body.position.y =
