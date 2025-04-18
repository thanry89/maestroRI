import streamlit as st
import pandas as pd

# Load data
data = pd.read_excel('data/maestroRI.xlsx', dtype=str)

site = st.selectbox(
    'Seleccionar Sitio',
    data['Nombre del Sitio'].sort_values().tolist(),
    index=None,
    placeholder='Seleccionar Sitio...'
    )

st.dataframe(data[data['Nombre del Sitio'] == site], hide_index=True, height=90, width=3000)
