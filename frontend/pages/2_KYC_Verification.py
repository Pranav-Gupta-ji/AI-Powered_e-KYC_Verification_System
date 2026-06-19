import requests
import streamlit as st

# ---------------------------------------------------
# Authentication Check
# ---------------------------------------------------

if "token" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

st.set_page_config(
    page_title="KYC Verification",
    page_icon="🪪",
    layout="wide"
)

st.title("🪪 e-KYC Verification System")
st.markdown("Upload an Aadhaar card and a selfie for verification.")

st.divider()

# ---------------------------------------------------
# Upload Section
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    document = st.file_uploader(
        "Upload Aadhaar Card",
        type=["jpg", "jpeg", "png", "pdf"]
    )

with col2:
    selfie = st.file_uploader(
        "Upload Selfie",
        type=["jpg", "jpeg", "png"]
    )

# ---------------------------------------------------
# Preview
# ---------------------------------------------------

if document or selfie:

    st.subheader("Preview")

    c1, c2 = st.columns(2)

    with c1:
        if document:
            if document.type.startswith("image"):
                st.image(
                    document,
                    caption="Uploaded Aadhaar",
                    use_container_width=True
                )
            else:
                st.info("PDF uploaded successfully.")

    with c2:
        if selfie:
            st.image(
                selfie,
                caption="Uploaded Selfie",
                use_container_width=True
            )

st.divider()

# ---------------------------------------------------
# Verify Button
# ---------------------------------------------------

if st.button("🔍 Verify KYC", use_container_width=True):

    if document is None or selfie is None:
        st.warning("Please upload both files.")
        st.stop()

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    files = {
        "document": (
            document.name,
            document.getvalue(),
            document.type
        ),
        "selfie": (
            selfie.name,
            selfie.getvalue(),
            selfie.type
        )
    }

    with st.spinner("Performing OCR, Face Verification and Database Check..."):

        response = requests.post(
            "http://127.0.0.1:8000/kyc/verify",
            headers=headers,
            files=files
        )

    # ---------------------------------------------------
    # SUCCESS
    # ---------------------------------------------------

    if response.status_code == 200:

        result = response.json()

        st.success("✅ Verification Completed Successfully")

        status = result.get("status")

        # ==========================
        # Existing Customer
        # ==========================

        if status == "already_registered":

            customer = result["customer"]

            st.info("Customer already exists in the database.")

            st.subheader("Customer Information")

            c1, c2 = st.columns(2)

            with c1:
                st.metric("Customer ID", customer["customer_id"])
                st.metric("Name", customer["name"])
                st.metric("Gender", customer["gender"])

            with c2:
                st.metric("DOB", customer["dob"])
                st.metric("Aadhaar", customer["aadhaar_number"])

        # ==========================
        # New Customer
        # ==========================

        else:

            details = result["details"]

            st.success("🎉 New customer registered successfully.")

            st.subheader("Extracted KYC Information")

            c1, c2 = st.columns(2)

            with c1:
                st.metric("Customer ID", result["customer_id"])
                st.metric("Name", details["name"])
                st.metric("Gender", details["gender"])

            with c2:
                st.metric("DOB", details["dob"])
                st.metric("Aadhaar Number", details["aadhaar_number"])

        st.divider()

        with st.expander("View API Response"):
            st.json(result)

    # ---------------------------------------------------
    # ERROR
    # ---------------------------------------------------

    else:

        st.error("Verification Failed")

        try:
            st.json(response.json())
        except:
            st.error(response.text)