import streamlit as st


def display_results(data):

    st.subheader("Extracted Information")

    col1, col2 = st.columns(2)

    with col1:

        st.text_input("Name", data.get("name", ""))

        st.text_input("DOB", data.get("dob", ""))

        st.text_input("Gender", data.get("gender", ""))

    with col2:

        st.text_input("Aadhaar", data.get("aadhaar_number", ""))

        