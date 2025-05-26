from typing import Dict, List
from app.models.lead import Lead  # Assuming Lead model is defined in lead.py
from fastapi import HTTPException

class LeadService:
    def __init__(self):
        self.leads_db: Dict[int, Lead] = {}
        self.current_id = 1

    def get_all_leads(self) -> List[Lead]:
        """Get all leads"""
        return list(self.leads_db.values())

    def get_lead(self, lead_id: int) -> Lead:
        """Get a specific lead by ID"""
        if lead_id not in self.leads_db:
            raise HTTPException(status_code=404, detail="Lead not found")
        return self.leads_db[lead_id]

    def create_lead(self, lead: Lead) -> Lead:
        """Create a new lead"""
        lead.id = self.current_id
        self.leads_db[self.current_id] = lead
        self.current_id += 1
        return lead

    def update_lead(self, lead_id: int, lead: Lead) -> Lead:
        """Update a lead"""
        if lead_id not in self.leads_db:
            raise HTTPException(status_code=404, detail="Lead not found")
        lead.id = lead_id
        self.leads_db[lead_id] = lead
        return lead

    def delete_lead(self, lead_id: int) -> Dict[str, str]:
        """Delete a lead by ID"""
        if lead_id not in self.leads_db:
            raise HTTPException(status_code=404, detail="Lead not found")
        del self.leads_db[lead_id]
        return {"message": "Lead deleted successfully"}