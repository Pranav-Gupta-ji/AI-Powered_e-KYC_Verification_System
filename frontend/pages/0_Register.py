import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Create Account")
st.caption("Register to access the E-KYC Verification System")

with st.form("register_form"):

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Create Account")

if submit:

    if not username or not email or not password:
        st.error("Please fill all fields.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:

        response = requests.post(
            f"{API_URL}/auth/register",
            json={
                "username": username,
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:

            st.success("✅ Registration Successful!")

            st.info("Go to the Login page to continue.")

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error("Registration failed.")