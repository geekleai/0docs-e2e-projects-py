from app.models import Opportunity

class OpportunityService:
    """Service for managing opportunities in the CRM system."""

    # In-memory storage (in a real app, this would be a database)
    opportunities_list: dict[int, Opportunity] = {}

    def get_all_opportunities(self) -> dict[str, dict[int, Opportunity]]:
        """Get all opportunities"""
        return {"opportunities": self.opportunities_list}

    def add_opportunity(self, opportunity: Opportunity) -> dict[str, Opportunity]:
        """Add a new opportunity"""
        self.opportunities_list[opportunity.id] = opportunity
        return {"opportunity": opportunity}

    def get_opportunity(self, opportunity_id: int) -> dict[str, Opportunity]:
        """Get a specific opportunity by ID"""
        if opportunity_id not in self.opportunities_list:
            raise ValueError("Opportunity not found")
        return {"opportunity": self.opportunities_list[opportunity_id]}

    def update_opportunity(self, opportunity_id: int, opportunity: Opportunity) -> dict[str, Opportunity]:
        """Update an opportunity by ID"""
        if opportunity_id not in self.opportunities_list:
            raise ValueError("Opportunity not found")
        self.opportunities_list[opportunity_id] = opportunity
        return {"opportunity": opportunity}

    def delete_opportunity(self, opportunity_id: int) -> dict[str, str]:
        """Delete an opportunity by ID"""
        if opportunity_id not in self.opportunities_list:
            raise ValueError("Opportunity not found")
        del self.opportunities_list[opportunity_id]
        return {"message": "Opportunity deleted successfully"}