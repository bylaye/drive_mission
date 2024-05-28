from pydantic import BaseModel
from typing import Optional

class MissionEnginBase(BaseModel):
    idMission: Optional[int]
    codeMission: Optional[str] = None
    idEngin: Optional[int] 
    immatricule: Optional[str] = None
    idPartenaire: Optional[int] = None


class MissionEnginResponse(MissionEnginBase):
    pass

