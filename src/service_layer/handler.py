import datetime
from typing import Dict
from src.domain.commands import CreatePatient, UpdatePatientDetails, DeletePatient
from src.domain.events import PatientCreated ,PatientDeleted
from src.domain import commands, events
from src.service_layer.unit_of_work import MongoUnitOfWork
from src.domain.model import PatientModel

from datetime import date

# Gestionnaire de commandes
class PatientCommandHandler:
    def __init__(self, uow:MongoUnitOfWork):
        self.uow = uow
        

    def handle_create_patient(self, command: commands.CreatePatient)->Dict[str,str]:
        
        patient_create_dict=command.dict()
        json_obj = {
        "active": True,
        "name": [
            {
                "family": patient_create_dict['family_name'],
                "given" : patient_create_dict["given_name"],
                "text": patient_create_dict['family_name'] +' '+ " ".join(patient_create_dict["given_name"]),
            }],
        "gender":patient_create_dict["gender"],
        "telecom": [
            {
            "system": "phone",
            "use": "mobile",
            "value": patient_create_dict["phone_number"]
            }
        ],
        "birthDate": patient_create_dict["birthdate"]
        }
        
        pat = PatientModel.parse_obj(json_obj)
        patient = pat.dict()
        print("conversion du patient en dictionnaire")
        if 'birthDate' in patient:
            birth_date = patient['birthDate']
            if isinstance(birth_date, date):
                patient['birthDate'] = datetime.datetime(birth_date.year, birth_date.month, birth_date.day)
        # Créer l'événement PatientCreated
        # patient_created_event = events.PatientCreated(
        #     family_name=command.family_name,
        #     given_name=command.given_name,
        #     phone_number=command.phone_number,
        #     gender=command.gender,
        #     birthdate=command.birthdate,
        # )
        

        # Publier l'événement PatientCreated
        # self.uow.event_publisher.publish(patient_created_event)
        result = self.uow.repository.save_patient(patient)
        print("handle_create_patient",result)
        return result
           
       

    def handle_update_patient_details(self, command: commands.UpdatePatientDetails):
        # Vérifier si le patient existe dans le système
        patient = self.uow.repository.get_patient_by_id(command.patient_id)
        if not patient:
            raise ValueError("Patient with the specified ID not found.")

        # Mettre à jour les détails du patient
        self.uow.update_patient(command.patient_id, command)

        # Créer l'événement PatientUpdated
        patient_updated_event = events.PatientUpdatedEvent(
            patient_id=command.patient_id,
            family_name=command.family_name,
            given_name=command.given_name,
            phone_number=command.phone_number,
            gender=command.gender,
            birthdate=command.birthdate,
        )

        # Publier l'événement PatientUpdated
        # self.uow.event_publisher.publish(patient_updated_event)

    def handle_delete_patient(self, command: commands.DeletePatient):
       
        # Supprimer le patient
        self.uow.repository.delete_patient(command)

        # Créer l'événement PatientDeleted
        patient_deleted_event = events.PatientDeletedEvent(patient_id=command.patient_id)



class PatientEventHandler:
    def __init__(self, uow:MongoUnitOfWork):
        self.uow = uow

    def handle_patient_created(self, Event: events.PatientCreated):
       
        pass
    def handle_delete_patient(self, Event: events.PatientDeleted):
       
        pass
   
   
#Initialisation du unity of work

uow=MongoUnitOfWork()   

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
    