from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List
import models


def get_engin_chauffeur(db:Session, idChauffeur:int):
    chauffeur = None
    if idChauffeur:
        chauffeur = db.query(models.EnginModel).filter(models.EnginModel.idChauffeur==idChauffeur).first()
    return chauffeur


def get_engin_all(db:Session):
    return db.query(models.EnginModel).all()


def get_engin_immatricule(db:Session, immatricule:int):
    db_immatricule = db.query(models.EnginModel).filter(models.EnginModel.immatricule==immatricule).first()
    return db_immatricule


def get_chauffeur_with_engin(db:Session, idChauffeur:int):
    req = text("""SELECT idEngin,  immatricule, e.idChauffeur, codePermanent, prenom, nom, telephone FROM Engin as e
            INNER JOIN Chauffeur as c ON e.idChauffeur=c.idChauffeur WHERE e.idChauffeur=:idChauffeur""")
    
    result = db.execute(req, {"idChauffeur": idChauffeur})
    rows = result.fetchall()
    if rows:
        cols = result.keys()
        return dict(zip(cols, rows[0]))
    return None


def get_chauffeur_all(db:Session):
    return db.query(models.ChauffeurModel).all()


def get_chauffeur_engin_with_code_permanent(db:Session, codePermanent:str):
    req = text("""SELECT idEngin, immatricule, e.idChauffeur, codePermanent, prenom, nom, telephone FROM Engin as e
            INNER JOIN 
               (SELECT codePermanent, idChauffeur, prenom, nom, telephone 
               FROM Chauffeur WHERE codePermanent=:codePermanent ) as c 
            ON e.idChauffeur=c.idChauffeur """)
    result = db.execute(req, {"codePermanent": codePermanent})
    rows = result.fetchall()
    if rows:
        cols = result.keys()
        return dict(zip(cols, rows[0]))
    return None


def get_chauffeur_by_id(db:Session, idChauffeur: int):
    db_code_permanent = db.query(models.ChauffeurModel).filter(models.ChauffeurModel.idChauffeur == idChauffeur).first()
    return db_code_permanent


def get_chauffeur_by_code_permanent(db:Session, codePermanent: str):
    db_code_permanent = db.query(models.ChauffeurModel).filter(models.ChauffeurModel.codePermanent == codePermanent).first()
    return db_code_permanent


def get_mission_all(db:Session):
    return db.query(models.MissionModel).all()


def get_mission_by_id(db:Session, idMission:int):
    return db.query(models.MissionModel).filter(models.MissionModel.idMission==idMission).first()


def get_partenaire_all(db:Session):
    return db.query(models.PartenaireModel).all()


def get_partenaire_by_id(db:Session, idPartenaire:int):
    return db.query(models.PartenaireModel).filter(models.PartenaireModel.idPartenaire==idPartenaire).first()


def get_mission_with_partenaire(db:Session, idMission:int):
    req = text("""SELECT idMission, typeMission, description, debutMission, finMission, 
               quantite, statusMission, idPartenaire, nomPartenaire
            FROM(
                    (SELECT * FROM Mission WHERE idMission=:idMission) as m 
                    INNER JOIN (SELECT idPartenaire as id, nomPartenaire FROM Partenaire) as p 
                    ON p.id =  m.idPartenaire
               )
               """)
    result = db.execute(req, {"idMission": idMission})
    rows = result.fetchall()
    if rows:
        cols = result.keys()
        return dict(zip(cols, rows[0]))
    return None


def get_partenaire_mission_by_name(db:Session, nomPartenaire:int):
    req = text("""SELECT idMission, typeMission, description, debutMission, finMission, 
               quantite, statusMission, idPartenaire, nomPartenaire
            FROM(
                    (SELECT idPartenaire as id, nomPartenaire FROM Partenaire WHERE nomPartenaire=:nomPartenaire) as p
                    INNER JOIN      
                    (SELECT * FROM Mission) as m ON p.id =  m.idPartenaire
               )
               """)
    result = db.execute(req, {"nomPartenaire": nomPartenaire})
    rows = result.fetchall()
    data = []
    cols = result.keys()
    if rows:
        for row in rows:
            data.append(dict(zip(cols, row)))
        return data
    return None