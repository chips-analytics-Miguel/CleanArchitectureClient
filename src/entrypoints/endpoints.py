from typing import Dict, List
from fastapi import APIRouter
from src.domain.commands import CreatePatient, UpdatePatientDetails, DeletePatient
from src.service_layer.messageBus import MessageBus
from src.domain.events import PatientCreated ,PatientDeleted
from src.service_layer.unit_of_work import MongoUnitOfWork
from src.domain.commands import CreatePatient
from src.domain.model import PatientModel
# from src.service_layer.queryhandler import Queryhandler
# from src.service_layer.commandhandler import Commandhandler
from circuitbreaker import circuit, CircuitBreaker
from src.service_layer.handler import PatientCommandHandler ,PatientEventHandler

import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)
class Circuitbreaker(CircuitBreaker):
        FAILURE_THRESHOLD = 5
        RECOVERY_TIMEOUT = 60
        EXPECTED_EXCEPTION = Exception

router = APIRouter(prefix="/api/v1/patient")

# #command handlers
# @router.post("/", status_code=201)
# @circuit(cls=CircuitBreaker)
# def create_patient(patient:PatientCreateSchema)-> Dict[str, str]:
#     patient_dict=patient.dict()
#     json_obj = {
#         "active": True,
#         "name": [
#             {
#                 "family": patient_dict['family_name'],
#                 "given" : patient_dict["given_name"],
#                 "text": patient_dict['family_name'] +' '+ " ".join(patient_dict["given_name"]),
#             }],
#         "gender":patient_dict["gender"],
#         "telecom": [
#             {
#             "system": "phone",
#             "use": "mobile",
#             "value": patient_dict["phone_number"]
#             }
#         ],
#         "birthDate": patient_dict["birthdate"]
#         }
#     pat = PatientModel.parse_obj(json_obj)
#     patient = pat.dict()
#     return Commandhandler().create_patient(patient)

 #initialized the unity_of_work
uow = MongoUnitOfWork()

# Create instances of CommandHandler and EventHandler
command_handler = PatientCommandHandler(uow=uow)
event_handler = PatientEventHandler(uow=uow)

event_handlers = {
    PatientCreated: [event_handler.handle_patient_created],
    PatientDeleted:[event_handler.handle_delete_patient]
    
}

command_handlers = {
    CreatePatient: command_handler.handle_create_patient,
    UpdatePatientDetails: command_handler.handle_update_patient_details,
    DeletePatient: command_handler.handle_delete_patient,
}


# Initialize the MessageBus with the Unit of Work and handlers
message_bus = MessageBus(uow, event_handlers=event_handlers, command_handlers=command_handlers)

# # Command handlers
@router.post("/", status_code=201)
def create_patient(patient: CreatePatient) -> Dict[str, str]:
    # Your existing code to create the patient command
    patient_dict = patient.dict()
    # ...
    
    # Create an instance of CreatePatient command
    create_patient_command = CreatePatient(
        family_name=patient_dict['family_name'],
        given_name=patient_dict["given_name"],
        phone_number=patient_dict["phone_number"],
        gender=patient_dict["gender"],
        birthdate=patient_dict["birthdate"]
    )

    # Instead of directly calling the Commandhandler, use the MessageBus
    result=message_bus.handle(create_patient_command)
    print( "endpoint",result)
    return message_bus.handle(create_patient_command)
    # return message_bus.test_func()
    
    


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

@router.get("/{patient_id}",response_model=PatientModel)
@circuit(cls=CircuitBreaker)
def get_patient_By_Id(patient_id: str)->PatientModel:
    return Queryhandler.get_patient_by_id(patient_id)
