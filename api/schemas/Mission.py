from pydantic import BaseModel
from pydantic import Field
from typing import Union
from typing import Optional
from typing import Literal
from datetime import datetime


class MissionStatus(BaseModel):
    statusMission: str = "RUN"


class MissionFin(BaseModel):
    finMission: Optional[datetime] = None


class MissionBase(BaseModel):
    entite: str = Field(..., description="Entite / Entreprise qui porte la mission")
    typeMission: str
    description: str
    quantite: Optional[float] = 0


class MissionCreate(MissionBase):
    debutMission: datetime = datetime.now()
    

class Mission(MissionBase, MissionFin, MissionStatus):
    idMission: int
    class Config:
        from_attributes = True