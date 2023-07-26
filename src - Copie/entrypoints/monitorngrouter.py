from fastapi import APIRouter, status
from src.domain.schemas_response import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def health_check() -> HealthResponse:
    """Checks the health of a project.

    :return: 200 if the project is healthy.
    """
    return HealthResponse()

