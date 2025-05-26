from pydantic import BaseModel
from typing import Optional

class Contact(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    customer_id: Optional[int] = None  # Reference to the associated customer
    lead_id: Optional[int] = None  # Reference to the associated lead

    class Config:
        orm_mode = True