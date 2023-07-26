from datetime import date
import datetime
from typing import Dict, List
from src.adapters.mongodb.mongoadapter import MongoDBAdapter
from src.domain.aggregats import Patient
from src.config import settings
from src.domain.exceptions import PatientException
from src.domain.schemas import PatientCreateSchema, PatientSchema
#from src.services_layers.eventshandler import
from src.adapters.celery_app import app as celery_app
from fastapi import HTTPException
import phonenumbers
from src.services_layers.eventshandler import EventHandler

collection = MongoDBAdapter(mongo_uri=settings.MONGO_URI)


def check_phone_number(number :str):
    number = phonenumbers.parse(number)
    return (phonenumbers.is_valid_number(number))


class PatientCommandServiceHandler(EventHandler,PatientException):
    """Patient Service Layer"""

    def create_patient(self,patient: dict) -> Dict[str,str]:
        if 'birthDate' in patient:
            birth_date = patient['birthDate']
            if isinstance(birth_date, date):
                patient['birthDate'] = datetime.datetime(birth_date.year, birth_date.month, birth_date.day)
        try:
            result = collection.save_patient(patient)
            task = celery_app.send_task('celery_app.create_patient_task', args=[result])
            self.PatientCreated(event_type="PatientCreated",event_data={"status": "Patient Created",result:patient})
        except Exception as e:
            raise HTTPException(status_code=400, detail = str(e))
        return {"patient_id":result,"task_id":task.id}

    def delete_patient(self,patient_id: str) -> Dict[str,str]:
        try:
            result = collection.del_patient(patient_id)
            if result == "NOT FOUND":
                raise self.PatientNotFoundError("Patient not found")
            task = celery_app.send_task('celery_app.del_patient_task', args=[patient_id])
            self.PatientCreated(event_type="PatientDeleted",event_data={patient_id:result})
        except self.PatientNotFoundError as e :
            raise HTTPException(status_code=400, detail = str(e))
        except Exception as e :
            raise HTTPException(status_code=400, detail = str(e))
        return {"patient_id":patient_id, "task_id":task.id, "status":result}


class PatientQueryServiceHandler:
    """Patient Query Service"""

    @classmethod
    def get_patient_by_id(cls, patient_id: str) -> PatientSchema:
        return collection.get_patient_by_id(patient_id)
    
    @classmethod
    def get_patients(cls) -> List[PatientSchema]:
        return collection.get_patients()