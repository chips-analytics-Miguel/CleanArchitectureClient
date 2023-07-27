from typing import List
from src.domain import commands, events
from src.service_layer.unit_of_work import MongoUnitOfWork

# Gestionnaire de commandes
class PatientCommandHandler:
    def __init__(self, uow):
        self.uow = MongoUnitOfWork()

    def handle_create_patient(self, command: commands.CreatePatient):
        # Vérifier si le patient existe déjà dans le système
        if self.uow.repository.get_by_id(command.patient_id):
            raise ValueError("Patient with the same ID already exists.")

        # Créer l'événement PatientCreated
        patient_created_event = events.PatientCreatedEvent(
            patient_id=command.patient_id,
            family_name=command.family_name,
            given_name=command.given_name,
            phone_number=command.phone_number,
            gender=command.gender,
            birthdate=command.birthdate,
        )

        # Publier l'événement PatientCreated
        self.uow.event_publisher.publish(patient_created_event)

    def handle_update_patient_details(self, command: commands.UpdatePatientDetails):
        # Vérifier si le patient existe dans le système
        patient = self.uow.patient_repository.get_by_id(command.patient_id)
        if not patient:
            raise ValueError("Patient with the specified ID not found.")

        # Mettre à jour les détails du patient
        patient.update_details(
            family_name=command.family_name,
            given_name=command.given_name,
            phone_number=command.phone_number,
            gender=command.gender,
            birthdate=command.birthdate,
        )

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
        self.uow.event_publisher.publish(patient_updated_event)

    def handle_delete_patient(self, command: commands.DeletePatient):
        # Vérifier si le patient existe dans le système
        patient = self.uow.patient_repository.get_by_id(command.patient_id)
        if not patient:
            raise ValueError("Patient with the specified ID not found.")

        # Supprimer le patient
        self.uow.patient_repository.delete(patient)

        # Créer l'événement PatientDeleted
        patient_deleted_event = events.PatientDeletedEvent(patient_id=command.patient_id)

        # Publier l'événement PatientDeleted
        self.uow.event_publisher.publish(patient_deleted_event)

# Gestionnaire d'événements
class PatientEventHandler:
    def __init__(self, uow):
        self.uow = uow

    def handle_patient_created(self, event: events.PatientCreatedEvent):
        # Enregistrer le nouveau patient dans la base de données
        patient = Patient(
            id=event.patient_id,
            family_name=event.family_name,
            given_name=event.given_name,
            phone_number=event.phone_number,
            gender=event.gender,
            birthdate=event.birthdate,
        )
        self.uow.patient_repository.add(patient)
