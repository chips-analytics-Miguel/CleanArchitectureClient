from abc import ABC, abstractmethod
from typing import List
from src.domain.aggregats import PatientModel
from src.domain.schemas import PatientCreateSchema


class AbstractRepository(ABC):

    @abstractmethod
    def save_patient(patient: PatientModel) -> str:
        pass

    @abstractmethod
    def get_patient_by_id(self, patient_id: str) -> PatientModel:
        pass
    
    @abstractmethod
    def get_patients(self) -> List[PatientModel]:
        pass

    @abstractmethod
    def update_patient(self, id: str, phone_number: str) -> PatientModel:
        pass

    """@abstractmethod
    def update_number(self, phone :str, newphone:str) -> PatientSchema:
        pass"""

    @abstractmethod
    def del_patient(self, patient_id: str) -> str:
        pass