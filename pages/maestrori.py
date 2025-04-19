import streamlit as st
import pandas as pd
from navigation import make_sidebar

st.set_page_config(page_title='Sitios RI', page_icon=None, layout="wide", initial_sidebar_state="collapsed")

make_sidebar()

st.title("Sitios RI")

# Load data
data = pd.read_excel('data/maestroRI.xlsx', dtype=str)

# Opciones
dic = {'Informacion': ['Codigo SISMAC', 'Nombre SISMAC', 'Cluster'],
           'Tecnología': ['Tecnología', 'RNC ID', 'ID 3G', 'Sitio 3G', 'ADJNODE ID', 'ID LTE', 'Sitio LTE', 'Celdas 3G - 1P', 'Celdas 3G - 2P', 'Celdas LTE AWS', 'Celdas LTE APT', 'Celdas LTE 1900'],
           'Ubicacion': ['Provincia', 'Cantón', 'Parroquia', 'Cuidad/Localidad', 'Latitud', 'Longitud', 'Dirección', 'Observaciones'],
            'Energia': ['Empresa Eléctrica', 'Contrato / CUE', 'Medidor', 'Generador', 'Estado Baterías'],
            'Infraestructura': ['Dueño Infraestructura', 'Codigo Torrero', 'Nombre Torrero', 'Equipamiento Coubicado', 'Tipo de Sitio', 'Altura Edificación', 'Tipo de Estructura ', 'Altura Estructura ', 'Altura total'],
            'Llaves': ['Fila', 'Columna', 'CENTRAL CNT REPOSO', 'ENTREGADA A SEGURIDAD', 'Ingreso 24/7'],
            'Direccionamiento IP': ['IP Gestion CoTX', 'IP Gestion 3G', 'IP Gestion LTE', 'IP Servicio 3G', 'IP Servicio LTE', 'IP RNC'],
            'Transmision': ['Medio de Transmision', 'Equipo Acceso 3G', 'Puerto Acceso 3G', 'Capa 3 3G', 'Equipo Acceso 4G', 'Puerto Acceso 4G', 'Capa 3 4G'],
            'Correctivos': ['Maleza', 'Correctivo', 'TX']
           }

opciones = list(dic.keys())

# Columnas
col1, col2 = st.columns(2)

with col1:
    site = st.selectbox(
        'Seleccionar Sitio',
        data['Nombre del Sitio'].sort_values().tolist(),
        index=None,
        placeholder='Seleccionar Sitio...'
    )

with col2:
    filter_cols = st.multiselect("Seleccionar Categoria", opciones, default=['Informacion', 'Energia', 'Ubicacion'])


if site:
    if filter_cols:
        for item in filter_cols:
            filtered_df = data[['Nombre del Sitio']+dic[item]][data['Nombre del Sitio'] == site]
            st.dataframe(filtered_df, hide_index=True, height=90, width=3000)
    else:
        st.dataframe(data[data['Nombre del Sitio'] == site], hide_index=True, height=90, width=3000)

    df_map = data[data['Nombre del Sitio'] == site][['Nombre del Sitio','Latitud', 'Longitud']]
    map_url = 'https://www.google.com/maps/place/'+ df_map['Latitud'] + ',' + df_map['Longitud']
    df_map[['Latitud', 'Longitud']] = df_map[['Latitud', 'Longitud']].astype('float')
    df_map.columns = ['Sitio','latitude', 'longitude']
    st.map(df_map, size=8, zoom=16)
    st.link_button(label='Google URL', url=map_url.iloc[0])