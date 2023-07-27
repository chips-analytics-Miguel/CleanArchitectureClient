from datetime import date
import datetime
from typing import Dict, List
from src.adapters.mongoadapter import MongoDBAdapter
from src.config import settings
from src.domain.aggregats import PatientModel
from src.domain.exceptions import PatientException
from src.domain.schemas import PatientCreateSchema
#from src.services_layers.eventshandler import
from src.adapters.celery_app import app as celery_app
from fastapi import HTTPException
import phonenumbers
from src.services_layers.eventshandler import EventHandler

collection = MongoDBAdapter(mongo_uri=settings.MONGO_URI)


class Queryhandler:
    """Patient Query Service"""

    @classmethod
    def get_patient_by_id(cls, patient_id: str) -> PatientModel:
        return collection.get_patient_by_id(patient_id)
    
    @classmethod
    def get_patients(cls) -> List[PatientModel]:
        return collection.get_patients()