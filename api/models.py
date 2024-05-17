import sys
import os
from mydb import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Date


class EnginModel(Base):
    __tablename__ = "Engin"
    idEngin = Column(Integer, primary_key=True)
    immatricule = Column(String(10), unique=True, index=True, nullable=False)
    marque = Column(String(20), index=True)
    typeEngin = Column(String(30))
    typeFuel = Column(String(30))
    capacite = Column(Float, default=0)
    is_remorque = Column(Boolean, default=False)
    created_at = Column(DateTime)
    annee = Column(Integer)
    idChauffeur = Column(Integer, ForeignKey('Chauffeur.idChauffeur'), unique=True, nullable=True)
    chauffeur = relationship("ChauffeurModel", back_populates="engin", uselist=False)
    rechargeFuel = relationship("RechargeFuelModel", back_populates="engin")
    deplacement = relationship("DeplacementModel", back_populates="engin")
    affecterEngin = relationship("AffecterModel", back_populates="engin")


class RechargeFuelModel(Base):
    __tablename__ = "RechargeFuel"
    idRechargeFuel = Column(Integer, primary_key=True)
    idEngin = Column(Integer, ForeignKey('Engin.idEngin'))
    dateRecharge = Column(DateTime)
    totalLitre = Column(Float)
    engin = relationship("EnginModel", back_populates="rechargeFuel")


class ChauffeurModel(Base):
    __tablename__ = "Chauffeur"
    idChauffeur = Column(Integer, primary_key=True)
    codePermanent = Column(String(30), unique=True, index=True, nullable=False)
    prenom = Column(String(40), nullable=False)
    nom = Column(String(40), nullable=False)
    adresse = Column(String(40), nullable=False)
    telephone = Column(String(20), nullable=True, unique=True)
    dateNaissance = Column(Date, nullable=False)
    is_active =  Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime)
    engin = relationship("EnginModel", back_populates="chauffeur",  uselist=False)


class MissionModel(Base):
    __tablename__ = 'Mission'
    idMission = Column(Integer, primary_key=True)
    typeMission = Column(String(30), index=True)
    description = Column(String(255))
    debutMission = Column(DateTime)
    finMission = Column(DateTime)
    quantite = Column(Float)
    statusMission = Column(String(20))
    idPartenaire = Column(Integer, ForeignKey('Partenaire.idPartenaire'), nullable=True)
    deplacement = relationship("DeplacementModel", back_populates="mission")
    affecterMission = relationship("AffecterModel", back_populates="mission")
    partenaire = relationship("PartenaireModel", back_populates="mission")


class PartenaireModel(Base):
    __tablename__ = 'Partenaire'
    idPartenaire = Column(Integer, primary_key=True)
    nomPartenaire = Column(String(50), unique=True, index=True, nullable=False)
    adressePartenaire = Column(String(100))
    emailPartenaire = Column(String(50),  unique=True, nullable=True)
    telephonePartenaire = Column(String(20), unique=True)
    mission = relationship("MissionModel", back_populates="partenaire")


class DeplacementModel(Base):
    __tablename__ = 'Deplacement'
    idDeplacement = Column(Integer, primary_key=True)
    depart = Column(DateTime, index=True )
    arrivee = Column(DateTime)
    typeCharge = Column(String(25), index=True )
    quantiteCharge = Column(Float)
    statusDeplacement = Column(String(20))
    idEngin = Column(Integer, ForeignKey('Engin.idEngin'))
    engin = relationship("EnginModel", back_populates="deplacement")
    idMission = Column(Integer, ForeignKey('Mission.idMission'))
    mission = relationship("MissionModel", back_populates="deplacement")


class AffecterModel(Base):
    __tablename__ ='Affecter'
    idAffecter = Column(Integer, primary_key=True)
    debutAffectation = Column(DateTime)
    finAffectation = Column(DateTime)
    statusAffectation = Column(String(20))
    idEngin = Column(Integer, ForeignKey('Engin.idEngin'))
    idMission = Column(Integer, ForeignKey('Mission.idMission'))
    engin = relationship("EnginModel", back_populates="affecterEngin")
    mission = relationship("MissionModel", back_populates="affecterMission")