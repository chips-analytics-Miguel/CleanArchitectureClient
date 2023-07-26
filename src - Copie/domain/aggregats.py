from typing import List, Optional
from fhir.resources.patient import PatientCommunication, PatientContact , PatientLink
from fhir.resources.identifier import Identifier
from fhir.resources.reference import Reference
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.address import Address
from fhir.resources.codeableconcept import CodeableConcept
from pydantic import BaseModel
from datetime import date
from src.domain.valuesobjects import AdministrativeGender


class Patient(BaseModel):
    patient_id : str
    identifier:List[Identifier]
    active: bool
    name: HumanName
    telecom: List[ContactPoint]
    gender: List[AdministrativeGender]
    birthDate: date
    deceased: bool  
    address: List[Address]
    maritalStatus: List[Optional[CodeableConcept]]
    multipleBirth: Optional[bool]
    contact: Optional[List[PatientContact]]
    link: Optional[List[PatientLink]]
    communication: Optional[List[PatientCommunication]]
    generalPractitioner: Optional[List[Reference]]
    managingOrganization: Optional[Reference]