from datetime import date
import datetime
from typing import Dict, List
from src.adapters.mongoadapter import MongoDBAdapter
from src.config import settings
from src.domain.model import PatientModel
from fastapi import HTTPException
import phonenumbers
from src.service_layer.eventshandler import EventHandler

collection = MongoDBAdapter(mongo_uri=settings.MONGO_URI)

def check_phone_number(number :str):
    number = phonenumbers.parse(number)
    return (phonenumbers.is_valid_number(number))

class Commandhandler(EventHandler):
    """Patient command handler"""

    def create_patient(self,patient: dict) -> Dict[str,str]:
        if 'birthDate' in patient:
            birth_date = patient['birthDate']
            if isinstance(birth_date, date):
                patient['birthDate'] = datetime.datetime(birth_date.year, birth_date.month, birth_date.day)
        try:
            result = collection.save_patient(patient)
            self.PatientCreated(event_type="PatientCreated",event_data={"status": "Patient Created",result:patient})
        except Exception as e:
            raise HTTPException(status_code=400, detail = str(e))
        return {"patient_id":result}

    def delete_patient(self,patient_id: str) -> Dict[str,str]:
        try:
            result = collection.del_patient(patient_id)
            if result == "NOT FOUND":
                raise self.PatientNotFoundError("Patient not found")
            self.PatientCreated(event_type="PatientDeleted",event_data={patient_id:result})
        except self.PatientNotFoundError as e :
            raise HTTPException(status_code=400, detail = str(e))
        except Exception as e :
            raise HTTPException(status_code=400, detail = str(e))
        return {"patient_id":patient_id, "status":result}