from pydantic import BaseModel
from pydantic import Field
from typing import Union
from typing import Optional
from typing import Literal
from datetime import datetime, date


class ChauffeurStatus(BaseModel):
    is_active: bool = True


class ChauffeurTelephone(BaseModel):
    telephone: str


class ChauffeurAdresse(BaseModel):
    adresse: str


class ChauffeurBase(ChauffeurStatus, ChauffeurAdresse, ChauffeurTelephone):
    codePermanent: str = Field(..., description="Serie Identification Chauffeur")
    prenom: str
    nom: str
    dateNaissance: Optional[date] = None


class ChauffeurCreate(ChauffeurBase):
    created_at: datetime = datetime.now()


class ChauffeurTelephoneUpdate(ChauffeurTelephone):
    pass


class ChauffeurAdresseUpdate(ChauffeurAdresse):
    pass

class Chauffeur(ChauffeurBase):
    idChauffeur: int 
    class Config:
        from_attributes = True
