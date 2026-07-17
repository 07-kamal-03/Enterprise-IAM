from __future__ import annotations

from fastapi import FastAPI

def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""
    
    application = FastAPI(
        title="Enterprise IAM",
        description=(
            "Enterprise Identity and Access Management (IAM) "
            "service providing authentication, authorization, "
            "and user management APIs."
        ),
        version="0.1.0",
    )
    
    return application

app = create_application()