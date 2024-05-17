from sqlalchemy.orm import Session
from schemas.Engin import Engin, EnginCreate
from schemas.Chauffeur import Chauffeur, ChauffeurCreate
from schemas.Mission import Mission, MissionCreate
from schemas.Partenaire import Partenaire, PartenaireCreate
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


def add_mission(db:Session, mission=MissionCreate):
    db_mission = models.MissionModel(**mission.model_dump())
    db.add(db_mission)
    db.commit()
    return db_mission


def add_partenaire(db:Session, partenaire=PartenaireCreate):
    db_partenaire = models.PartenaireModel(**partenaire.model_dump())
    db.add(db_partenaire)
    db.commit()
    return db_partenaire