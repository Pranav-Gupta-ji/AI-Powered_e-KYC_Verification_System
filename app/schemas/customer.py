from pydantic import BaseModel
from typing import Optional


class CustomerResponse(BaseModel):

    id: int

    name: Optional[str]

    dob: Optional[str]

    gender: Optional[str]

    aadhaar_number: str

    class Config:
        from_attributes = True