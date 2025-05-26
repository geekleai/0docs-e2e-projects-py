from fastapi import APIRouter, HTTPException
from typing import Dict, List
from app.schemas.contact import Contact
from app.services.contact_service import ContactService

router = APIRouter(
    prefix="/contacts",
    tags=["contacts"],
    responses={404: {"description": "Not found"}},
)

contact_service = ContactService()

@router.get("/", response_model=List[Contact])
def get_contacts():
    """Get all contacts"""
    return contact_service.get_all_contacts()

@router.get("/{contact_id}", response_model=Contact)
def get_contact(contact_id: int):
    """Get a specific contact by ID"""
    contact = contact_service.get_contact(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.post("/", response_model=Contact)
def create_contact(contact: Contact):
    """Create a new contact"""
    return contact_service.create_contact(contact)

@router.put("/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, contact: Contact):
    """Update a contact"""
    updated_contact = contact_service.update_contact(contact_id, contact)
    if updated_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated_contact

@router.delete("/{contact_id}")
def delete_contact(contact_id: int):
    """Delete a contact by ID"""
    success = contact_service.delete_contact(contact_id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}