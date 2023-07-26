from typing import List
from pydantic import BaseModel

from src.domain.valuesobjects import Systeme, Use, UseName


class Name(BaseModel):
    use: UseName
    family : str
    given: List[str]

class Telecom(BaseModel):
    system: Systeme
    value : str
    use: Use

class Address(BaseModel):
    use : Use
    line : List[str]
    city : str
    district :str
    state : str
    postalCode : str