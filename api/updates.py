from sqlalchemy.orm import Session
from sqlalchemy.sql import text
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


def update_engin_chauffeur_with_immatricule_code_permanent(db:Session, immatricule:str, chauffeur_update:EnginChauffeurUpdate):
    engin_data = reads.get_engin_immatricule(db=db, immatricule=immatricule)
    if engin_data:
        engin_unassign = update_engin_unassign_with_immatricule(db=db, immatricule=immatricule)
        if engin_unassign:
            codePermanent = chauffeur_update.model_dump()['codePermanent']
            db_chauffeur = reads.get_chauffeur_by_code_permanent(db=db, codePermanent=codePermanent)
            update_unassign_chauffeur_engin_with_code_permanent(db=db, codePermanent=codePermanent)
            if db_chauffeur:
                idChauffeur = db_chauffeur.idChauffeur
                req = text("""
                        UPDATE Engin SET idChauffeur=:idChauffeur
                        WHERE immatricule=:immatricule 
                    """)
                result = db.execute(req, {"immatricule": immatricule, "idChauffeur": idChauffeur})
                db.commit()
                return reads.get_chauffeur_engin_with_code_permanent(db=db, codePermanent=codePermanent)
    return None


def update_engin_unassign_with_immatricule(db:Session, immatricule:str):
    db_engin = reads.get_engin_immatricule(db=db, immatricule=immatricule)
    if db_engin:
        db_engin.idChauffeur = None
        db.commit()
        db.refresh(db_engin)
        return db_engin
    return None


def update_unassign_chauffeur_engin_with_code_permanent(db:Session, codePermanent:str):
    db_chauffeur = reads.get_chauffeur_engin_with_code_permanent(db=db, codePermanent=codePermanent)
    if db_chauffeur:
        req = text("""
                UPDATE Engin SET idChauffeur = NULL
                WHERE idChauffeur = (SELECT idChauffeur FROM Chauffeur WHERE codePermanent=:codePermanent)
                """)
        result = db.execute(req, {"codePermanent": codePermanent})
        db.commit()
        return reads.get_engin_by_id(db=db, idEngin=db_chauffeur['idEngin'])
    return None


def update_fin_mission(db:Session, idMission:int, mission_update:MissionUpdateFin):
    mission_data = db.query(models.MissionModel).filter(models.MissionModel.idMission==idMission).first()
    if mission_data:
        mission_data.finMission = mission_update.model_dump()["finMission"]
        db.commit()
        db.refresh(mission_data)

        return reads.get_mission_with_partenaire(db=db, idMission=idMission)
    else:
        return None


def update_fin_mission_by_code(db:Session, codeMission:str, mission_update:MissionUpdateFin):
    mission_data = db.query(models.MissionModel).filter(models.MissionModel.codeMission==codeMission).first()
    print(mission_data.finMission)
    if mission_data:
        idMission = mission_data.idMission
        mission_data.finMission = mission_update.model_dump()["finMission"]
        db.commit()
        db.refresh(mission_data)

        #return reads.get_mission_with_partenaire(db=db, idMission=idMission)
        return reads.get_mission_by_code(db=db, codeMission=codeMission)
    else:
        return None
