from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from datetime import datetime


class DeplacementStatus(BaseModel):
    statusDeplacement: Optional[str] = "RUN"


class DeplacementFin(BaseModel):
    arrivee: datetime = datetime.now()


class DeplacementBase(DeplacementStatus):
    idEngin: int
    idMission: int
    typeCharge: str
    quantiteCharge: float

    
class DeplacementCreate(DeplacementBase):
    depart: datetime = datetime.now()


class Deplacement(DeplacementBase):
    idDeplacement: int