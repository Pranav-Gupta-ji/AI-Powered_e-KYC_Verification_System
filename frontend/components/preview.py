from PIL import Image
import streamlit as st


def show_preview(uploaded_file):

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Document",
        use_container_width=True,
    )