from fastapi import APIRouter, HTTPException
from typing import Dict, List
from app.schemas.lead import Lead
from app.services.lead_service import LeadService

router = APIRouter(
    prefix="/leads",
    tags=["leads"],
    responses={404: {"description": "Not found"}},
)

lead_service = LeadService()

@router.get("/", response_model=List[Lead])
def get_all_leads():
    """Get all leads"""
    return lead_service.get_all_leads()

@router.get("/{lead_id}", response_model=Lead)
def get_lead(lead_id: int):
    """Get a specific lead by ID"""
    lead = lead_service.get_lead(lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@router.post("/", response_model=Lead)
def create_lead(lead: Lead):
    """Create a new lead"""
    return lead_service.create_lead(lead)

@router.put("/{lead_id}", response_model=Lead)
def update_lead(lead_id: int, lead: Lead):
    """Update a lead"""
    updated_lead = lead_service.update_lead(lead_id, lead)
    if updated_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return updated_lead

@router.delete("/{lead_id}")
def delete_lead(lead_id: int):
    """Delete a lead by ID"""
    success = lead_service.delete_lead(lead_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lead not found")
    return {"message": "Lead deleted successfully"}