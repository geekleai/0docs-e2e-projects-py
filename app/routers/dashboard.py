from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"],
)

@router.get("/stats")
def get_dashboard_stats() -> Dict[str, Any]:
    """Get dashboard statistics"""
    return {
        "total_customers": 150,
        "total_leads": 75,
        "total_opportunities": 30,
        "conversion_rate": "20%",
        "last_updated": "2023-10-01T12:00:00Z"
    }

@router.get("/health")
def health_check() -> Dict[str, str]:
    """Health check for the dashboard"""
    return {
        "status": "healthy",
        "timestamp": "2023-10-01T12:00:00Z"
    }