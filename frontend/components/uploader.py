import streamlit as st

def upload_file():

    uploaded = st.file_uploader(

        "Upload Aadhaar Card",

        type=[
            "jpg",
            "jpeg",
            "png",
            "pdf"
        ]
    )

    return uploaded