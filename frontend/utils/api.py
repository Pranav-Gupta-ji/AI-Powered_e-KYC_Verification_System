import requests
from utils.config import API_URL


def process_document(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type,
        )
    }

    response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        return response.json()

    raise Exception(response.text)