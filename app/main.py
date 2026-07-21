from __future__ import annotations

from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings

def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""
    
    application = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version,
    )
    
    application.include_router(health_router)
    
    return application

app = create_application()