from pydantic import BaseModel
from pydantic import EmailStr
from typing import Union
from typing import Optional
from typing import Literal
from datetime import datetime


class PartenaireBase(BaseModel):
    nomPartenaire: str
    adressePartenaire: Optional[str] = None
    telephonePartenaire: Optional[str] = None
    emailPartenaire: Optional[EmailStr] = None


class PartenaireCreate(PartenaireBase):
    pass


class Partenaire(PartenaireBase):
    idPartenaire: int
    class Config:
        from_attributes = True