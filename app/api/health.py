from __future__ import annotations

from fastapi import APIRouter, status

from app.schemas.health import HealthResponse
from app.services.health_service import HealthService

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

health_service = HealthService()

@router.get(
    "",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
)

def get_health_status() -> HealthResponse:
    """Endpoint to check the health status of the application."""
    
    return health_service.get_health_status()