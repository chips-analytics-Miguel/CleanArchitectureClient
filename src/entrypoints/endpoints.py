from typing import Dict, List
from fastapi import APIRouter
from src.domain.commands import CreatePatient, UpdatePatientDetails, DeletePatient
from src.service_layer.messageBus import MessageBus
from src.service_layer.handler import uow, event_handlers ,command_handlers
from src.domain.commands import CreatePatient
from src.domain.model import PatientModel
from circuitbreaker import circuit, CircuitBreaker
from src.service_layer.handler import PatientCommandHandler ,PatientEventHandler
import pybreaker
breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)
class Circuitbreaker(CircuitBreaker):
        FAILURE_THRESHOLD = 5
        RECOVERY_TIMEOUT = 60
        EXPECTED_EXCEPTION = Exception

router = APIRouter(prefix="/api/v1/patient")

# Initialize the MessageBus with the Unit of Work and handlers
message_bus = MessageBus(uow, event_handlers=event_handlers, command_handlers=command_handlers)


@router.post("/", status_code=201)
@circuit(cls=CircuitBreaker)
def create_patient(patient: CreatePatient) -> Dict[str, str]:
   
    patient_dict = patient.dict()

  
    create_patient_command = CreatePatient(
        family_name=patient_dict['family_name'],
        given_name=patient_dict["given_name"],
        phone_number=patient_dict["phone_number"],
        gender=patient_dict["gender"],
        birthdate=patient_dict["birthdate"]
    )

  
    result=message_bus.handle(create_patient_command)
    return {"patient_id":result}
  
    


# @router.delete("/{patient_id}")
# @circuit(cls=CircuitBreaker)
# def delete_patient(patient_id: str)->Dict[str, str]:
#     return Commandhandler().delete_patient(patient_id)

"""@router.patch("/{phone_number}")
@circuit(cls=CircuitBreaker)
def update_phone_number(id: str,newphone:str)->PatientSchema:
    return PatientCommandServiceHandler.update_phone_number(patient_id=id,newphone=newphone)
@router.put("/{patient_id}")
@circuit(cls=CircuitBreaker)
def update_patient_by_id(patient_id: str, patient: PatientSchema)->PatientSchema:
    return PatientCommandServiceHandler.update_patient(id=patient_id, patient=patient)
"""

# # Queries handlers
# @router.get("/",response_model=List[PatientModel])
# @circuit(cls=CircuitBreaker)
# def get_patients()->List[PatientModel]:
#     return Queryhandler.get_patients()

# @router.get("/{patient_id}",response_model=PatientModel)
# @circuit(cls=CircuitBreaker)
# def get_patient_By_Id(patient_id: str)->PatientModel:
#     return Queryhandler.get_patient_by_id(patient_id)
