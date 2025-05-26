from fastapi import APIRouter, HTTPException
from typing import Dict, List
from app.schemas.opportunity import OpportunityCreate, OpportunityUpdate, Opportunity
from app.services.opportunity_service import OpportunityService

router = APIRouter(
    prefix="/opportunities",
    tags=["opportunities"],
    responses={404: {"description": "Not found"}},
)

opportunity_service = OpportunityService()

@router.post("/", response_model=Opportunity)
def create_opportunity(opportunity: OpportunityCreate):
    """Create a new opportunity"""
    return opportunity_service.create_opportunity(opportunity)

@router.get("/", response_model=List[Opportunity])
def get_opportunities():
    """Get all opportunities"""
    return opportunity_service.get_all_opportunities()

@router.get("/{opportunity_id}", response_model=Opportunity)
def get_opportunity(opportunity_id: int):
    """Get a specific opportunity by ID"""
    opportunity = opportunity_service.get_opportunity(opportunity_id)
    if opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return opportunity

@router.put("/{opportunity_id}", response_model=Opportunity)
def update_opportunity(opportunity_id: int, opportunity_update: OpportunityUpdate):
    """Update an opportunity"""
    updated_opportunity = opportunity_service.update_opportunity(opportunity_id, opportunity_update)
    if updated_opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return updated_opportunity

@router.delete("/{opportunity_id}")
def delete_opportunity(opportunity_id: int):
    """Delete an opportunity by ID"""
    success = opportunity_service.delete_opportunity(opportunity_id)
    if not success:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return {"message": "Opportunity deleted successfully"}