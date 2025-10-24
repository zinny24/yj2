import pandas as pd
import folium
import streamlit as st

from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.set_page_config(page_title="2025년 전국지역별 축제", layout="wide")
st.sidebar.header("필터 옵션")

df = pd.read_csv("events_100.csv")

category = df["category"].unique().tolist()
sel_cate = st.sidebar.multiselect("카테고리 선택", category, default=category)

regions = df["region"].unique().tolist()
sel_reg = st.sidebar.multiselect("지역 선택", regions, default=regions)

filtered_df = df[ df["category"].isin(sel_cate) & df["region"].isin(sel_reg) ]

st.write(f'총 {len(filtered_df)} 개의 지역 이벤트 표시 중')

m = folium.Map( location=[df["lat"].mean(), df["lon"].mean()], zoom_start=8 )

m_cluster = MarkerCluster().add_to(m)

category_colors = {
    "축제" : "red",
    "공연" : "blue",
    "체험" : "green",
    "문화" : "purple",
    "과학" : "orange",
    "전시" : "cadeblue",
    "전통" : "darkred"
}

for _, row in filtered_df.iterrows():
    c = category_colors.get(row["category"], "black")

    img_html = f'<img src="{row['img']}" width="100" height="100" style="float:left">'
    
    popup_box = f'''
        <div style="width:300px";margin-left:20px;>
            {img_html}
            <div style="overflow:hidden">
                <h4>{row['title']}</h4>
                <span style="font-size:12px">카테고리 : { row["category"] }</span><br>
                <span style="font-size:12px">기간 : { row["start_date"] }  ~ {row["end_date"]}</span><br>
                <span style="font-size:12px">대상연령: { row["target_age"] }</span><br>
                <span style="font-size:12px">대상성별 : { row["target_gender"] }</span><br>
                <span style="font-size:12px">태그 : { row["tags"] }</span><br>
                <span style="font-size:12px"> <a href='{row["url"]}' target="_blank">홈페이지</a>  </span>
            </div>
        </div>
    '''
    
    folium.Marker(
        location=[  row["lat"], row["lon"] ],
        tooltip=row["title"],
        icon=folium.Icon(color=c),
        popup=folium.Popup(popup_box, max_width=300)
    ).add_to(m_cluster)

st_folium(m, width=1000, height=700)


