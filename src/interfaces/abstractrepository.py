from abc import ABC, abstractmethod
from typing import List
from src.domain.schemas import PatientCreateSchema
#from src.domain.entities import PatientModel


class PatientInterface(ABC):

    @abstractmethod
    def save_patient(patient: PatientCreateSchema) -> str:
        pass

    @abstractmethod
    def get_patient_by_id(self, patient_id: str) -> PatientCreateSchema:
        pass
    
    @abstractmethod
    def get_patients(self) -> List[PatientCreateSchema]:
        pass

    @abstractmethod
    def update_patient(self, id: str, phone_number: str) -> PatientCreateSchema:
        pass

    """@abstractmethod
    def update_number(self, phone :str, newphone:str) -> PatientSchema:
        pass"""

    @abstractmethod
    def del_patient(self, patient_id: str) -> None:
        pass