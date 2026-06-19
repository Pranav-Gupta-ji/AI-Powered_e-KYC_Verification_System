import os
import shutil

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.core.config import settings

from app.core.auth_dependency import (
    get_current_user
)

from app.services.ocr_service import (
    extract_text
)

from app.services.aadhaar_service import (
    extract_aadhaar,
    extract_kyc_details
)

from app.services.face_service import (
    verify_faces
)

from app.services.customer_service import (
    get_customer_by_aadhaar,
    create_customer
)

router = APIRouter(
    prefix="/kyc",
    tags=["KYC"]
)

#========================
# Save Upload Helper
#========================

def save_upload(
    file: UploadFile,
    directory: str
):

    os.makedirs(
        directory,
        exist_ok=True
    )

    path = os.path.join(
        directory,
        file.filename
    )

    with open(path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return path

#=========================
# Verify KYC Endpoint
#=========================
@router.post("/verify")
def verify_kyc(
    document: UploadFile = File(...),
    selfie: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    document_path = save_upload(
        document,
        settings.UPLOAD_DOC_DIR
    )

    selfie_path = save_upload(
        selfie,
        settings.UPLOAD_SELFIE_DIR
    )

    text = extract_text(
        document_path
    )

    aadhaar_number = (
        extract_aadhaar(text)
    )

    details = (
        extract_kyc_details(text)
    )

    if not aadhaar_number:

        raise HTTPException(
            status_code=400,
            detail="Aadhaar not found"
        )

    existing = get_customer_by_aadhaar(
    db,
    aadhaar_number
    )

    if existing:

        return {
            "status": "already_registered",
            "message": "Customer already exists in the database.",
            "customer": {
                "customer_id": existing.id,
                "name": existing.name,
                "dob": existing.dob,
                "gender": existing.gender,
                "aadhaar_number": existing.aadhaar_number
            }
        }

    face_result = verify_faces(
        document_path,
        selfie_path
    )

    if not face_result.get(
        "verified"
    ):

        raise HTTPException(
            status_code=400,
            detail="Face mismatch"
        )

    customer = create_customer(
        db=db,
        name=details["name"],
        dob=details["dob"],
        gender=details["gender"],
        aadhaar_number=aadhaar_number,
        document_path=document_path,
        selfie_path=selfie_path
    )

    return {
    "status": "success",
    "customer_id": customer.id,
    "details": {
        "name": details["name"],
        "dob": details["dob"],
        "gender": details["gender"],
        "aadhaar_number": aadhaar_number
    }
}