import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('data/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['expiry_days']
)

authenticator.login(key='Entrar', location='main')

if st.session_state["authentication_status"]:
    st.sidebar.subheader(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout('Salir', 'sidebar')
    st.switch_page('maestrori.py')

elif st.session_state["authentication_status"] == False:
    st.error('Usuario o Contraseña incorrectos')