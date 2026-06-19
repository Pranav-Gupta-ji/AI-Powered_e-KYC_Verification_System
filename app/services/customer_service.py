from sqlalchemy.orm import Session

from app.db.models import Customer

from app.core.logger import logger


def get_customer_by_aadhaar(
    db: Session,
    aadhaar_number: str
):

    customer = (

        db.query(Customer)

        .filter(
            Customer.aadhaar_number
            == aadhaar_number
        )

        .first()
    )

    return customer

def create_customer(
    db: Session,
    name: str,
    dob: str,
    gender: str,
    aadhaar_number: str,
    document_path: str,
    selfie_path: str
):

    customer = Customer(

        name=name,

        dob=dob,

        gender=gender,

        aadhaar_number=aadhaar_number,

        document_path=document_path,

        selfie_path=selfie_path
    )

    db.add(customer)

    db.commit()

    db.refresh(customer)

    logger.info(
        f"Customer created: "
        f"{aadhaar_number}"
    )

    return customer

def get_customer(
    db: Session,
    customer_id: int
):

    return (

        db.query(Customer)

        .filter(
            Customer.id
            == customer_id
        )

        .first()
    )

