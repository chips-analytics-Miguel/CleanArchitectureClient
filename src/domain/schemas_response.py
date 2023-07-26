from datetime import datetime

from pydantic import BaseModel

from src.config import settings


class HealthResponse(BaseModel):
    """Health Check Response Model."""

    app_name: str = settings.APP_NAME
    app_version: str = settings.APP_VERSION
    status: str = "pass"
    timestamp: datetime = datetime.now()