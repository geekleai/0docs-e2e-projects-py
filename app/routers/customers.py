from fastapi import APIRouter, HTTPException
from typing import List, Dict
from app.schemas.customer import CustomerCreate, CustomerUpdate, Customer
from app.services.customer_service import CustomerService

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)

customer_service = CustomerService()

@router.post("/", response_model=Customer)
def create_customer(customer: CustomerCreate) -> Customer:
    """Create a new customer"""
    return customer_service.create_customer(customer)

@router.get("/", response_model=List[Customer])
def get_customers() -> List[Customer]:
    """Get all customers"""
    return customer_service.get_all_customers()

@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: int) -> Customer:
    """Get a specific customer by ID"""
    customer = customer_service.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer_update: CustomerUpdate) -> Customer:
    """Update a customer"""
    updated_customer = customer_service.update_customer(customer_id, customer_update)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int) -> Dict[str, str]:
    """Delete a customer"""
    success = customer_service.delete_customer(customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}