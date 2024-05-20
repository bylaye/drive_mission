from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from datetime import datetime


class AffecterFin(BaseModel):
    finAffectation: Optional[datetime] = None


class AffecterStatus(BaseModel):
    statusAffectation: Optional[str] = "RUN"


class AffecterBase(AffecterStatus):
    idEngin: int
    idMission: int
    debutAffectation: datetime = datetime.now()
    

class AffecterCreate(AffecterBase):
    pass


class AffecterFinUpdate(AffecterFin):
    pass 


class AffecterStatusUpdate(AffecterStatus):
    pass 


class Affecter(AffecterBase, AffecterFin):
    idAffecter: int