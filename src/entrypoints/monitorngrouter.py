from fastapi import APIRouter, status
from datetime import datetime

from pydantic import BaseModel

from src.config import settings


class HealthResponse(BaseModel):
    """Health Check Response Model."""

    app_name: str = settings.APP_NAME
    app_version: str = settings.APP_VERSION
    status: str = "pass"
    timestamp: datetime = datetime.now()

router = APIRouter()

@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def health_check() -> HealthResponse:
    """Checks the health of a project.

    :return: 200 if the project is healthy.
    """
    return HealthResponse()

