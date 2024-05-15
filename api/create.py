from sqlalchemy.orm import Session
from schemas.Engin import Engin, EnginCreate
from schemas.Chauffeur import Chauffeur, ChauffeurCreate
from typing import List
import models


def add_engin(db: Session, engin=EnginCreate):
    db_engin = models.EnginModel(**engin.model_dump())
    db.add(db_engin)
    db.commit()
    return db_engin


def add_chauffeur(db: Session, chauffeur=ChauffeurCreate):
    #print(chauffeur.model_dump())
    db_chauffeur = models.ChauffeurModel(**chauffeur.model_dump())
    db.add(db_chauffeur)
    db.commit()
    return db_chauffeur