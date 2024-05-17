from sqlalchemy.orm import Session
from schemas.Engin import EnginChauffeurUpdate
from schemas.Mission import MissionUpdateFin, MissionUpdateStatus
import reads
import models


def update_engin_chauffeur(db:Session, idEngin:int, chauffeur_update:EnginChauffeurUpdate):
    engin_data = db.query(models.EnginModel).filter(models.EnginModel.idEngin == idEngin).first()
    if engin_data:
        idChauffeur = engin_data.idChauffeur
        for k, v in chauffeur_update.dict().items():
            setattr(engin_data, k, v)
        get_chauffeur = reads.get_chauffeur_with_engin(db=db, idChauffeur=idChauffeur)
        if not get_chauffeur:
            db.commit()
            db.refresh(engin_data)
            get_chauffeur = reads.get_chauffeur_with_engin(db=db, idChauffeur=engin_data.idChauffeur)
        return get_chauffeur
    else:
        return None


def update_fin_mission(db:Session, idMission:int, mission_update:MissionUpdateFin):
    mission_data = db.query(models.MissionModel).filter(models.MissionModel.idMission==idMission).first()
    if mission_data:
        mission_data.finMission = mission_update.model_dump()["finMission"]
        db.commit()
        db.refresh(mission_data)
        return mission_data
    else:
        return None