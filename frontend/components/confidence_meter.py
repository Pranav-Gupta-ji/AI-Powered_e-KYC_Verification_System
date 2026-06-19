import streamlit as st


def show_confidence(score):

    st.subheader("OCR Confidence")

    st.progress(score / 100)

    st.metric(
        "Confidence",
        f"{score:.2f}%"
    )