# app/db/models.py

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from datetime import datetime

from app.db.database import Base


# =========================================
# User Model
# =========================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Customer(Base):

    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=True
    )

    dob = Column(
        String,
        nullable=True
    )

    gender = Column(
        String,
        nullable=True
    )

    aadhaar_number = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    document_path = Column(
        String,
        nullable=False
    )

    selfie_path = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )