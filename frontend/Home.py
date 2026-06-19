import streamlit as st

st.set_page_config(
    page_title="AI e-KYC Verification System",
    page_icon="🪪",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("frontend/assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title="AI e-KYC Verification System",
    page_icon="🪪",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("frontend/assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================================
# Hero Section
# =====================================================

st.title("🪪 AI-Powered e-KYC Verification System")

st.markdown("""
### Secure • Automated • Intelligent Customer Verification

An end-to-end AI-powered e-KYC platform that automates identity verification using
Optical Character Recognition (OCR), Face Verification, and Customer Data Management.

The system extracts information from Aadhaar documents, verifies user identity through
facial matching, detects existing customers, and securely stores verified customer records.
""")

# =====================================================
# Project Overview
# =====================================================

st.subheader("📌 Project Overview")

st.markdown("""
This project demonstrates a complete production-style e-KYC workflow:

✅ User Authentication using JWT

✅ Aadhaar OCR Data Extraction

✅ Face Verification using Computer Vision

✅ Duplicate Customer Detection

✅ Customer Database Management

✅ REST API with FastAPI

✅ Interactive Frontend with Streamlit

✅ Containerized Deployment using Docker
""")

# =====================================================
# Use Cases
# =====================================================

st.subheader("🏢 Industry Use Cases")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
**🏦 Banking & Finance**

• Digital Account Opening

• Loan Verification

• Customer Onboarding

• Fraud Prevention
""")

with col2:
    st.info("""
**🛡️ Insurance**

• Policy Enrollment

• Identity Verification

• Claim Validation

• Customer Authentication
""")

with col3:
    st.info("""
**📱 FinTech & Telecom**

• e-KYC Registration

• SIM Verification

• Digital Wallet Onboarding

• Regulatory Compliance
""")

# =====================================================
# Architecture
# =====================================================

st.subheader("⚙️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.metric("Backend", "FastAPI")

with tech2:
    st.metric("Frontend", "Streamlit")

with tech3:
    st.metric("OCR Engine", "EasyOCR")

with tech4:
    st.metric("CV Library", "OpenCV")

# =====================================================
# Skills Demonstrated
# =====================================================

st.subheader("🎯 Skills Demonstrated")

st.markdown("""
### Artificial Intelligence & Machine Learning
- OCR-based Information Extraction
- Image Processing
- Face Verification
- Computer Vision

### Backend Engineering
- FastAPI Development
- REST API Design
- JWT Authentication
- Database Integration

### Data Engineering
- Data Validation
- Customer Data Management
- Structured Data Storage

### DevOps & Deployment
- Docker Containerization
- Environment Configuration
- API Documentation

### Software Engineering
- Modular Project Architecture
- Error Handling
- Authentication & Authorization
- Production-Oriented Development
""")

# =====================================================
# Developer Profile
# =====================================================

st.subheader("👨‍💻 Developer")

st.markdown("""
**Pranav Gupta**

Data Scientist & AI Engineer passionate about Artificial Intelligence,
Machine Learning, Computer Vision, Data Science, and Backend Development.

This project demonstrates practical implementation of:
- AI & Computer Vision
- OCR Systems
- FastAPI Development
- Streamlit Applications
- Database Integration
- Docker Deployment
""")

# =====================================================
# Personal Branding
# =====================================================

st.subheader("🌐 Connect With Me")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/pranavguptaji/"
    )

with col2:
    st.link_button(
        "GitHub",
        "https://github.com/Pranav-Gupta-ji"
    )

with col3:
    st.link_button(
        "Portfolio",
        "https://pranav-gupta-ji.github.io/"
    )

# =====================================================
# Footer
# =====================================================

st.caption(
    "AI-Powered e-KYC Verification System | Built with FastAPI, EasyOCR, OpenCV, Docker, and Streamlit"
)