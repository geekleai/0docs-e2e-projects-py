from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Opportunity(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    value: float
    status: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()