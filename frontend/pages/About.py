import streamlit as st

st.title("ℹ️ About")

st.markdown("""
## AI-Powered e-KYC Verification System

This application automates the Know Your Customer (KYC) verification process using Optical Character Recognition (OCR), face verification, and a secure REST API.

### 🛠️ Technology Stack

- 🚀 FastAPI
- 👁️ EasyOCR
- 📷 OpenCV
- 🐳 Docker
- 🎨 Streamlit

---

### 📚 API Documentation

The backend exposes a REST API built with FastAPI.

You can explore and test all available endpoints using the interactive Swagger UI.

""")

st.link_button(
    "🚀 Open FastAPI API Documentation",
    "http://127.0.0.1:8000/docs",
    use_container_width=True
)

if st.sidebar.button("Logout"):

    del st.session_state["token"]

    st.rerun()