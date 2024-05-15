from pydantic import BaseModel
from pydantic import Field
from typing import Union
from typing import Optional
from typing import Literal
from datetime import datetime


class EnginChauffeurId(BaseModel):
    idChauffeur: Optional[int] = None


class EnginCapacite(BaseModel):
    capacite: Union[float, int] = 0
    is_remorque: bool = False


class EnginBase(EnginCapacite, EnginChauffeurId):
    immatricule: str = Field(..., description="Immatriculation de Engin") # type: ignore
    marque: str = None
    typeEngin: str = None
    annee: Optional[int] = None
    typeFuel: str = "GASOIL"
    

class EnginCreate(EnginBase):
    created_at: datetime = datetime.now()


class EnginUpdate(EnginCapacite):
    pass


class Engin(EnginBase):
    idEngin: int
    

    class Config:
        from_attributes = True


class EnginCHauffeurCodePermanent(BaseModel):
    codePermanent: str


class EnginChauffeur(EnginChauffeurId, EnginCHauffeurCodePermanent):
    idEngin :int
    immatricule:  Optional[str] = None
    prenom:  Optional[str] = None
    nom: Optional[str] = None
    telephone:  Optional[str] = None


class EnginChauffeurUpdate(EnginChauffeurId):
    pass


class EnginChauffeurUpdateCodePermanent(EnginCHauffeurCodePermanent):
    pass