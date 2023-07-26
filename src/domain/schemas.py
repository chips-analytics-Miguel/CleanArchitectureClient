from datetime import date, datetime
from typing import List
from pydantic import BaseModel

from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName

from src.domain.entities import Address, Name, Telecom
from src.domain.valuesobjects import Gender


class PatientModel(Patient, BaseModel):
    # Définissez les champs que vous voulez inclure dans le modèle PatientModel
    name: List[HumanName]

class HumanNameSchema(BaseModel):
    text: str

"""class PatientSchema(BaseModel):
    active: bool
    name: List[HumanNameSchema]"""
class PatientModel(Patient):
    pass

class PatientCreateSchema(BaseModel):

    family_name : str
    given_name : List[str]
    phone_number: str
    gender: str
    birthdate: date

class PatientSchema(BaseModel):
    resourceType : str = "Patient"
    active : bool
    name: List[Name]
    telecom: List[Telecom]
    gender: Gender
    birthDate: date
    address: List[Address] 