import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from navigation import make_sidebar

st.set_page_config(page_title='O&M RI', page_icon=None, layout="centered", initial_sidebar_state="collapsed")

with open('data/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['expiry_days']
)
authenticator.login(key='Entrar', location='main')

make_sidebar()

if st.session_state["authentication_status"]:
    st.sidebar.subheader(f'Bienvenido *{st.session_state["name"]}*')
    authenticator.logout('Salir', 'sidebar')
    st.title('Seleccionar Opción:')
    if st.button("Sitios RI"):
        st.switch_page('pages/maestrori.py')
    if st.button("Trafico Celdas"):
        st.switch_page('pages/celdas.py')

elif st.session_state["authentication_status"] == False:
    st.error('Usuario o Contraseña incorrectos')