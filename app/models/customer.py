from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    created_at: str
    updated_at: str