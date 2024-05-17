from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from datetime import datetime


class RechargeFuelBase(BaseModel):
    idEngin: int
    totalLitre: float
    dateRecharge: datetime = datetime.now()


class RechargeFuelCreate(RechargeFuelBase):
    pass 


class RechargeFuel(RechargeFuelBase):
    idRechargeFuel: int


    class Config:
        from_attributes = True


class RechargeFuelEnginResponse(RechargeFuelBase):
    immatricule: str