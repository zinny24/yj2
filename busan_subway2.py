# ----------------------------
# 1. 라이브러리 불러오기
# ----------------------------
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# ----------------------------
# 2. 페이지 설정
# ----------------------------
st.set_page_config(page_title="부산 지하철 승객 지도", layout="wide")
st.title("🚌 부산 지하철 역별 승객 지도")

# ----------------------------
# 3. 데이터 불러오기
# ----------------------------
df = pd.read_csv("busan_subway_passengers.csv", encoding="utf-8")

# ----------------------------
# 4. 사이드바 인터랙션 (CSV 기반 min/max)
# ----------------------------
st.sidebar.header("지도 필터 옵션")

min_passengers = int(df["승객수"].min())
max_passengers = int(df["승객수"].max())

threshold = st.sidebar.slider(
    "붐비는 역 기준 승객수",
    min_value=min_passengers,
    max_value=max_passengers,
    value=int((min_passengers + max_passengers)/2),
    step=1000
)

# ----------------------------
# 5. 색상/반경 함수
# ----------------------------
def get_color(passengers, threshold):
    # threshold 이상 → 붐비는 역 빨강
    if passengers >= threshold:
        return "red"
    # threshold 미만 → 기본 색
    return "blue"

def scale_radius(passengers, threshold):
    # threshold 이상 → 확대
    if passengers >= threshold:
        return min(passengers / 2000 * 1.5, 30)
    # threshold 미만 → 기본 크기
    return max(5, min(passengers / 2000, 30))

# ----------------------------
# 6. 2분할 화면
# ----------------------------
col1, col2 = st.columns([1,2])

with col1:
    st.subheader("📌 옵션 및 안내")
    st.markdown(f"- 현재 붐비는 역 기준: **{threshold:,}명**")

with col2:
    st.subheader("🗺️ 승객수 지도")
    m = folium.Map(location=[35.1796, 129.0756], zoom_start=12)

    for idx, row in df.iterrows():
        lat = row['위도']
        lng = row['경도']
        name = row['역명']
        passengers = row['승객수']

        # CircleMarker 색상/반경 결정
        color = get_color(passengers, threshold)
        radius = scale_radius(passengers, threshold)

        # 팝업 HTML
        popup_html = f"""
        <div style="
            font-size:14px;
            font-weight:bold;
            color:#333;
            background-color:rgba(255,255,255,0.9);
            padding:6px 10px;
            border-radius:6px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
            text-align:center;
            font-family: 'Malgun Gothic', '맑은 고딕', sans-serif;
        ">
            <div>{name}</div>
            <div>승객수: {int(passengers):,}</div>
        </div>
        """

        # CircleMarker 추가
        folium.CircleMarker(
            location=[lat, lng],
            radius=radius,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6,
            popup=folium.Popup(popup_html, max_width=250)
        ).add_to(m)

        # threshold 이상인 역 이름 표시
        if passengers >= threshold:
            folium.map.Marker(
                location=[lat, lng],
                icon=folium.DivIcon(
                    html=f"""
                    <div style="
                        display:inline-block;
                        white-space:nowrap;
                        font-size:11px;
                        color:black;
                        font-weight:bold;
                        text-shadow: 1px 1px 2px white;
                        background-color: rgba(255,255,255,0.6);
                        padding: 2px 6px;
                        border-radius: 4px;
                        font-family: 'Malgun Gothic', '맑은 고딕', sans-serif;
                    ">
                    {name}
                    </div>
                    """
                )
            ).add_to(m)

    # Streamlit 지도 표시
    st_folium(m, width=800, height=800)
