import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status

from src.config import settings


@pytest.mark.anyio
async def test_health_check(client: AsyncClient, fastapi_app: FastAPI) -> None:
    """
    Checks the health endpoint.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """
    url = fastapi_app.url_path_for("health_check")
    response = await client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "pass"
    assert response.json()["app_name"] == settings.APP_NAME
    assert response.json()["app_version"] == settings.APP_VERSION
