from datetime import date, datetime
from typing import List
from pydantic import BaseModel


class PatientCreateSchema(BaseModel):

    family_name : str
    given_name : List[str]
    phone_number: str
    gender: str
    birthdate: date