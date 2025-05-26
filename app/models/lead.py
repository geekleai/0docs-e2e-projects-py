from pydantic import BaseModel
from typing import Optional

class Lead(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    status: str
    source: Optional[str] = None
    created_at: str
    updated_at: str