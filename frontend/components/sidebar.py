import streamlit as st
from streamlit_option_menu import option_menu

def show_sidebar():

    with st.sidebar:

        choice = option_menu(
            "Navigation",
            [
                "Home",
                "OCR Result",
                "API Docs",
                "About",
                "Settings"
            ],
            icons=[
                "house",
                "file-earmark-text",
                "code-slash",
                "info-circle",
                "gear"
            ],
            default_index=0,
        )

    return choice