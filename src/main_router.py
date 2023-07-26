from fastapi.routing import APIRouter
from src.entrypoints.monitorngrouter import router as monitoring_router
from src.entrypoints.patientrouter import router as patient_router

app_router = APIRouter()

app_router.include_router(
    monitoring_router,
    tags=["Health"],
)

app_router.include_router(
    patient_router,
    tags=["Patients"],
)