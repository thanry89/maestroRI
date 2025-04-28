import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx



def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = ctx.pages_manager.get_pages()

    return pages[ctx.page_script_hash]["page_name"]



def make_sidebar():
    with st.sidebar:
        st.title("O&M RI")

        if st.session_state.authentication_status:
            st.page_link("app.py", label="Inicio")
            st.page_link("pages/maestrori.py", label="Sitios RI", icon="🔒")
            st.page_link("pages/celdas.py", label="Estado Celdas", icon="🕵️")
            st.page_link("pages/poa.py", label="POA", icon="🕵️")

        elif get_current_page_name() != "app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("app.py")