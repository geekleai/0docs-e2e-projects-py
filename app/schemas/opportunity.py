from pydantic import BaseModel
from typing import Optional

class Opportunity(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    value: float
    status: str
    customer_id: int

class OpportunityCreate(BaseModel):
    title: str
    description: Optional[str] = None
    value: float
    status: str
    customer_id: int

class OpportunityUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    value: Optional[float] = None
    status: Optional[str] = None
    customer_id: Optional[int] = None