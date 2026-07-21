from __future__ import annotations

from app.schemas.health import HealthResponse

class HealthService:
    """Service responsible for application health checks."""
    
    def get_health_status(self) -> HealthResponse:
        """Return the current health status of the application."""
        
        return HealthResponse(
            status="healthy",
            service="Enterprise IAM",
            version="0.1.0"
        )