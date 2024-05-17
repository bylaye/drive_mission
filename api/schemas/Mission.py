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


class MissionBase(MissionStatus):
    idPartenaire: Optional[int] = None
    typeMission: str
    description: Optional[str] = None
    quantite: Optional[float] = 0


class MissionCreate(MissionBase):
    debutMission: datetime = datetime.now()
    

class Mission(MissionBase, MissionFin, MissionStatus):
    idMission: int
    class Config:
        from_attributes = True


class MissionUpdateFin(MissionFin):
    pass 


class MissionUpdateStatus(MissionStatus):
    pass


class MissionResponseUpdate(Mission, MissionCreate):
    nomPartenaire: str 