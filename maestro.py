import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd

with open('data/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['expiry_days']
)

try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state.get('authentication_status'):
    authenticator.logout()
    st.write(f'Welcome *{st.session_state.get("name")}*')
    st.title('Archivo Maestro')

    # Load data
    data = pd.read_excel('data/maestroRI.xlsx', dtype=str)

    site = st.selectbox(
        'Seleccionar Sitio',
        data['Nombre del Sitio'].sort_values().tolist(),
        index=None,
        placeholder='Seleccionar Sitio...'
    )

    st.dataframe(data[data['Nombre del Sitio'] == site], hide_index=True, height=90, width=3000)

elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')