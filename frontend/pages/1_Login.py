import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    response = requests.post(
        f"{API}/auth/login",
        json={
            "username": username,
            "password": password
        }
    )

    if response.status_code == 200:

        token = response.json()["access_token"]

        st.session_state.token = token
        st.session_state.logged_in = True
        st.session_state.username = username

        st.success("Login Successful")

    else:

        st.error(response.json()["detail"])

    
st.session_state.username = username

st.sidebar.success(
    f"Welcome {st.session_state.username}"
)