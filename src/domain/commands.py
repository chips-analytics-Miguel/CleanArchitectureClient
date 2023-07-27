from dataclasses import dataclass
from typing import List
from datetime import date

# Commande pour créer un nouveau patient
@dataclass(frozen=True)
class CreatePatient:
    family_name : str
    given_name : List[str]
    phone_number: str
    gender: str
    birthdate: date

# Commande pour mettre à jour les détails d'un patient
@dataclass(frozen=True)
class UpdatePatientDetails:
    patient_id: str
    name: str
    age: int
    address: str

# Commande pour supprimer un patient
@dataclass(frozen=True)
class DeletePatient:
    patient_id: str


