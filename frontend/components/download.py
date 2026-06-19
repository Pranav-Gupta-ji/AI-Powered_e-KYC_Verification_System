import json
import streamlit as st


def download_json(data):

    st.download_button(
        "Download JSON",
        json.dumps(data, indent=4),
        "ocr_result.json",
        "application/json",
    )