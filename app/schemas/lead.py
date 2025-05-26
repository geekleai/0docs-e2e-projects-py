from pydantic import BaseModel
from typing import Optional

class Lead(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    status: str
    created_at: str
    updated_at: str

class LeadCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    status: str

class LeadUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None