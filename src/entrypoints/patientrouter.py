from datetime import date, datetime
from typing import Dict
from fastapi import APIRouter
from src.config import settings
from src.domain.schemas import PatientCreateSchema, PatientModel, PatientSchema
from src.services_layers.commandsquerieshandler import PatientCommandServiceHandler,PatientQueryServiceHandler
#from src.interfaces.abstractrepository import PatientInterface
from circuitbreaker import circuit, CircuitBreaker
import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)
class Circuitbreaker(CircuitBreaker):
        FAILURE_THRESHOLD = 5
        RECOVERY_TIMEOUT = 60
        EXPECTED_EXCEPTION = Exception

router = APIRouter(prefix="/api/v1/patient")

@router.post("/test/")
async def create_patient(patient: PatientCreateSchema):
        patient_dict=patient.dict()
        json_obj = {
        "active": True,
        "name": [
            {
                "family": patient_dict['family_name'],
                "given" : patient_dict["given_name"],
                "text": patient_dict['family_name'] +' '+ " ".join(patient_dict["given_name"]),
            }],
        "gender":patient_dict["gender"],
        "telecom": [
            {
            "system": "phone",
            "use": "mobile",
            "value": patient_dict["phone_number"]
            }
        ],
        "birthDate": patient_dict["birthdate"]
        }
        pat = PatientModel.parse_obj(json_obj)
        patient = pat.dict()
        # # inserted_patient_id = patient_service.create_patient(patient_data)
        # # response_content = { "patient_id": inserted_patient_id }
        # # return JSONResponse(content=response_content)
        return patient

#command handlers
@router.post("/", status_code=201)
@circuit(cls=CircuitBreaker)
def create_patient(patient:PatientCreateSchema)-> Dict[str, str]:
    patient_dict=patient.dict()
    json_obj = {
        "active": True,
        "name": [
            {
                "family": patient_dict['family_name'],
                "given" : patient_dict["given_name"],
                "text": patient_dict['family_name'] +' '+ " ".join(patient_dict["given_name"]),
            }],
        "gender":patient_dict["gender"],
        "telecom": [
            {
            "system": "phone",
            "use": "mobile",
            "value": patient_dict["phone_number"]
            }
        ],
        "birthDate": patient_dict["birthdate"]
        }
    pat = PatientModel.parse_obj(json_obj)
    patient = pat.dict()
    return PatientCommandServiceHandler().create_patient(patient)

@router.delete("/{patient_id}")
@circuit(cls=CircuitBreaker)
def delete_patient(patient_id: str)->Dict[str, str]:
    return PatientCommandServiceHandler().delete_patient(patient_id)

"""@router.patch("/{phone_number}")
@circuit(cls=CircuitBreaker)
def update_phone_number(id: str,newphone:str)->PatientSchema:
    return PatientCommandServiceHandler.update_phone_number(patient_id=id,newphone=newphone)
@router.put("/{patient_id}")
@circuit(cls=CircuitBreaker)
def update_patient_by_id(patient_id: str, patient: PatientSchema)->PatientSchema:
    return PatientCommandServiceHandler.update_patient(id=patient_id, patient=patient)
"""

# Queries handlers
@router.get("/")
@circuit(cls=CircuitBreaker)
def get_patients()->PatientSchema:
    return PatientQueryServiceHandler.get_patients()

@router.get("/{patient_id}")
@circuit(cls=CircuitBreaker)
def get_patient_By_Id(patient_id: str)->PatientSchema:
    return PatientQueryServiceHandler.get_patient_by_id(patient_id)
