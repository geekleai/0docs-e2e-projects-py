from fastapi import APIRouter

router = APIRouter()

from .customers import router as customers_router
from .leads import router as leads_router
from .opportunities import router as opportunities_router
from .contacts import router as contacts_router
from .dashboard import router as dashboard_router

router.include_router(customers_router)
router.include_router(leads_router)
router.include_router(opportunities_router)
router.include_router(contacts_router)
router.include_router(dashboard_router)