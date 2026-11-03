import datetime
import requests
import pandas as pd
import streamlit as st

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 디자인
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="어제 박스오피스 순위",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 어제 일별 박스오피스 TOP 10")

# -----------------------------------------------------------------------------
# 2. 한국 시간(KST, UTC+9) 기준 어제 날짜 구하기
# -----------------------------------------------------------------------------
# 배포 서버(Streamlit Cloud)의 시계는 UTC(세계협정시) 기준일 수 있으므로,
# 한국 시간(UTC+9)을 명확하게 계산해서 어제 날짜를 구합니다.
utc_now = datetime.datetime.now(datetime.timezone.utc)
kst_now = utc_now + datetime.timedelta(hours=9)
yesterday = kst_now - datetime.timedelta(days=1)
target_dt = yesterday.strftime("%Y%m%d")  # KOBIS API 규격인 YYYYMMDD 형태 문자열

st.caption(f"📅 기준 날짜: {yesterday.strftime('%Y년 %m월 %d일')} (한국 시간 기준)")

# -----------------------------------------------------------------------------
# 3. Streamlit Secrets에서 API 인증키 불러오기
# -----------------------------------------------------------------------------
# Secrets에 KOBIS_KEY가 설정되어 있는지 확인합니다.
if "KOBIS_KEY" not in st.secrets or not st.secrets["KOBIS_KEY"]:
    st.error("⚠️ API 인증키(KOBIS_KEY)가 설정되지 않았습니다.")
    st.info("""
    **💡 확인 방법:**
    1. Streamlit Cloud의 앱 설정 화면으로 이동합니다.
    2. **Secrets** 메뉴를 선택합니다.
    3. 아래 형식으로 발급받은 API 키를 등록해 주세요:
       ```toml
       KOBIS_KEY = "발급받은_키_문자열"
       ```
    """)
    st.stop()

api_key = st.secrets["KOBIS_KEY"]

# -----------------------------------------------------------------------------
# 4. KOBIS API 데이터 요청
# -----------------------------------------------------------------------------
url = "https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
params = {
    "key": api_key,
    "targetDt": target_dt
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # HTTP 상태 코드 에러(4xx, 5xx) 체크
    data = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"⚠️ 영화진흥위원회(KOBIS) 서버와의 통신 중 오류가 발생했습니다: {e}")
    st.info("💡 인터넷 연결 상태를 확인하거나 잠시 후 다시 시도해 주세요.")
    st.stop()

# -----------------------------------------------------------------------------
# 5. 응답 데이터 검증 (faultInfo 응답 및 빈 데이터 예외 처리)
# -----------------------------------------------------------------------------
# KOBIS API는 키가 잘못되어도 200 OK와 함께 'faultInfo' 객체를 반환합니다.
if "faultInfo" in data:
    fault = data["faultInfo"]
    st.error(f"⚠️ API 인증 에러가 발생했습니다. (사유: {fault.get('message', '알 수 없음')})")
    st.info("""
    **💡 확인해야 할 사항:**
    1. Streamlit Secrets에 입력한 `KOBIS_KEY` 값이 정확한지 확인해 주세요.
    2. [KOBIS 영화관입장권통합전산망 오픈API](https://www.kobis.or.kr/kobisopenapi)에서 키 발급 및 활성화 상태를 확인해 주세요.
    """)
    st.stop()

# boxOfficeResult 내의 dailyBoxOfficeList 추출
box_office_result = data.get("boxOfficeResult", {})
daily_list = box_office_result.get("dailyBoxOfficeList", [])

# 영화 목록이 비어있는 경우 안내
if not daily_list:
    st.warning("⚠️ 어제 날짜의 박스오피스 데이터가 존재하지 않거나 아직 집계 전입니다.")
    st.info("""
    **💡 확인해야 할 사항:**
    - 한국 시간으로 이른 아침일 경우 어제 데이터 집계가 아직 완료되지 않았을 수 있습니다.
    - KOBIS 시스템 점검 시간인지 확인해 주세요.
    """)
    st.stop()

# -----------------------------------------------------------------------------
# 6. 데이터 전처리 (문자열 -> 숫자 변환)
# -----------------------------------------------------------------------------
df = pd.DataFrame(daily_list)

# KOBIS API의 숫자 값은 전부 문자열로 전송되므로 수치형으로 변환해 줍니다.
numeric_cols = ["rank", "rankInten", "audiCnt", "audiAcc", "scrnCnt", "showCnt"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------------------------------------------------------
# 7. 1위 영화 지표 카드 표시 (Metric 카드 3장)
# -----------------------------------------------------------------------------
top1 = df.iloc[0]  # 순위 1위 데이터

st.subheader(f"🥇 1위 영화: {top1['movieNm']}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="일일 관객수",
        value=f"{top1['audiCnt']:,}명",
        delta=f"전날 대비 순위 {top1['rankInten']:+}위" if top1['rankInten'] != 0 else "순위 변동 없음"
    )

with col2:
    st.metric(
        label="누적 관객수",
        value=f"{top1['audiAcc']:,}명"
    )

with col3:
    st.metric(
        label="스크린수 / 상영횟수",
        value=f"{top1['scrnCnt']:,}개",
        delta=f"총 {top1['showCnt']:,}회 상영",
        delta_color="off"
    )

st.markdown("---")

# -----------------------------------------------------------------------------
# 8. 관객수 상위 5편 막대그래프
# -----------------------------------------------------------------------------
st.subheader("📊 관객수 상위 5개 영화")

top5_df = df.head(5)[["movieNm", "audiCnt"]].copy()
# 막대그래프 세로축 정렬을 위해 영화명을 인덱스로 지정
top5_df = top5_df.rename(columns={"movieNm": "영화명", "audiCnt": "일일 관객수"})
top5_df = top5_df.set_index("영화명")

st.bar_chart(top5_df)

st.markdown("---")

# -----------------------------------------------------------------------------
# 9. 박스오피스 전체 순위 표 출력
# -----------------------------------------------------------------------------
st.subheader("📋 전체 박스오피스 순위 (TOP 10)")

# 필요한 컬럼만 추출하여 한글 명칭으로 변경
display_df = df[[
    "rank", "movieNm", "openDt", "audiCnt", "audiAcc", "scrnCnt"
]].copy()

display_df.columns = ["순위", "영화명", "개봉일", "관객수", "누적관객", "스크린수"]

# 천 단위 쉼표 포맷팅을 적용하여 Streamlit 대화형 표로 출력
st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "순위": st.column_config.NumberColumn(format="%d위"),
        "관객수": st.column_config.NumberColumn(format="%d명"),
        "누적관객": st.column_config.NumberColumn(format="%d명"),
        "스크린수": st.column_config.NumberColumn(format="%d개"),
    }
)
