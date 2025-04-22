import streamlit as st
import pandas as pd
from navigation import make_sidebar
import plotly.express as px
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title='Sitios RI', page_icon=None, layout="wide", initial_sidebar_state="collapsed")

make_sidebar()

st.title("Cumplimiento POA 2025")

poa = pd.read_excel(io='data/POA_2025_MOVIL.xlsx')

#st.dataframe(poa)

month = st.selectbox(
    'Seleccionar Mes',
    poa['Mes'].sort_values().unique(),
    index=None,
    placeholder='Seleccionar Mes...'
    )

if month:
    filt_df = poa[poa['Mes']==month]
    st.dataframe(filt_df)

    fig = px.pie(filt_df, names='Cumplido', width=500, height=500)
    st.plotly_chart(fig)

    df_map = filt_df[['DESC UBICACION','Latitud','Longitud','Cumplido']]
    df_map[['Latitud','Longitud']] = df_map[['Latitud','Longitud']].astype('float')
    df_map.columns = ['Sitio','lat','lon', 'Cumplido']
    
    m = folium.Map(location=[df_map['lat'].mean(), df_map['lon'].mean()], zoom_start=10)
                 
    for index, row in df_map.iterrows():
        if row['Cumplido'] == 'SI':
            folium.Marker(location=[row['lat'], row['lon']], tooltip=row['Sitio'], icon=folium.Icon(color='green')).add_to(m)
        else:
            folium.Marker(location=[row['lat'], row['lon']], tooltip=row['Sitio'], icon=folium.Icon(color='red')).add_to(m)
    st_data = st_folium(m, height=800, width = 1800)