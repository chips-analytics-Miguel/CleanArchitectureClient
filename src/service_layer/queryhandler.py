from datetime import date
import datetime
from typing import Dict, List
from src.adapters.mongoadapter import MongoDBAdapter
from src.config import settings
from src.domain.model import PatientModel
from src.domain.schemas import PatientCreateSchema
from fastapi import HTTPException
import phonenumbers
from src.service_layer.eventshandler import EventHandler

collection = MongoDBAdapter(mongo_uri=settings.MONGO_URI)


class Queryhandler:
    """Patient Query Service"""

    @classmethod
    def get_patient_by_id(cls, patient_id: str) -> PatientModel:
        return collection.get_patient_by_id(patient_id)
    
    @classmethod
    def get_patients(cls) -> List[PatientModel]:
        return collection.get_patients()