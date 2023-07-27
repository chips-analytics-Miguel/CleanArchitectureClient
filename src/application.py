from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from src import __version__
from src.lifetime import register_shutdown_event, register_startup_event
from src.entrypoints.endpoints import router as patient_router
from src.entrypoints.monitorngrouter import router as monitoring_router
from src.logging import configure_logging


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    configure_logging()
    app = FastAPI(
        title="Microservice Boilerplate",
        description="Starter project for microservice development using FastAPI",
        version=__version__,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=patient_router)
    app.include_router(router=monitoring_router)

    return app
