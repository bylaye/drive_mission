from mydb import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
import models 
from schemas.Engin import EnginCreate, Engin, EnginChauffeur, EnginChauffeurUpdate
from schemas.Chauffeur import Chauffeur, ChauffeurCreate
from schemas.Mission import Mission, MissionCreate
from schemas.Partenaire import Partenaire, PartenaireCreate
import create
import reads
import updates


models.Base.metadata.create_all(bind=engine)

ERROR_NOT_FOUND = 404

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engin_router = APIRouter(prefix="/engins", tags=["Engins"])


@engin_router.post("/add", response_model=Engin)
def create_engin(engin: EnginCreate, db: Session = Depends(get_db)):
    chauffeur = reads.get_chauffeur_by_id(db=db, idChauffeur=engin.idChauffeur)
    chauffeur_engin = reads.get_engin_chauffeur(db=db, idChauffeur=engin.idChauffeur)
    immatricule = reads.get_engin_immatricule(db=db, immatricule=engin.immatricule)
    if immatricule:
        raise HTTPException(status_code=404, detail=f"Immatricule {engin.immatricule} existe deja")
    
    if chauffeur or engin.idChauffeur == None:
        if chauffeur_engin:
            raise HTTPException(status_code=ERROR_NOT_FOUND, 
                            detail=f"Le chauffeur est deja au camion {chauffeur_engin.immatricule}")
        return create.add_engin(db=db, engin=engin)
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"chauffeur not found")            


@engin_router.get("/get/all/", response_model=List[Engin])
def get_engin_all(db:Session = Depends(get_db)):
    engins = reads.get_engin_all(db=db)
    if engins:
        return engins
    else:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Engin is empty")


@engin_router.get("/get/immatricule/{immatricule}", response_model=Engin)
def get_engin_by_immatricule( immatricule:str, db:Session = Depends(get_db)):
    db_immatricule=  reads.get_engin_immatricule(db=db, immatricule=immatricule)
    if db_immatricule:
        return db_immatricule
    else:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Immatricule {immatricule} not exists")
      

@engin_router.get("/get/chauffeur/{idChauffeur}", response_model=EnginChauffeur)
def get_chauffeur_with_engin(idChauffeur: int, db:Session = Depends(get_db)):
    chauffeur = reads.get_chauffeur_with_engin(db=db, idChauffeur=idChauffeur)
    if chauffeur:
        return chauffeur
    else:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Chauffeur {idChauffeur} not exists ")


@engin_router.get("/get/chauffeur/codepermanent/{codePermanent}", response_model=EnginChauffeur)
def get_chauffeur_engin_with_code_permanent(codePermanent: str, db:Session = Depends(get_db)):
    permanent = reads.get_chauffeur_engin_with_code_permanent(db=db, codePermanent=codePermanent)
    print(f' Permanent {permanent}')
    if permanent:
        return permanent
    else:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Engin avec Chauffeur {codePermanent} not found ")


@engin_router.put("/update/chauffeur/{idEngin}", response_model=EnginChauffeur)
def update_chauffeur_engin(idEngin:int, chauffeur_update:EnginChauffeurUpdate, db: Session = Depends(get_db)):
    idChauffeur = chauffeur_update.model_dump()['idChauffeur']
    db_chauffeur = reads.get_chauffeur_with_engin(db=db, idChauffeur=idChauffeur)
    
    if db_chauffeur:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Chauffeur engin {db_chauffeur}")
    else:
        db_update = updates.update_engin_chauffeur(db=db, idEngin=idEngin, chauffeur_update=chauffeur_update)
        if db_update:
            return db_update
        else:
            raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Engin not found")


# Chauffeur
chauffeur_router = APIRouter(prefix="/chauffeurs", tags=["Chauffeurs"])

@chauffeur_router.post("/add", response_model=Chauffeur)
def create_chauffeur(chauffeur:ChauffeurCreate, db: Session = Depends(get_db)):
    codePermanent = chauffeur.model_dump()['codePermanent']
    db_code_permanent = reads.get_chauffeur_by_code_permanent(db=db, codePermanent=codePermanent)
    if db_code_permanent:
        raise HTTPException(status_code=404, detail="Code Permanent deja enregistre")
    return create.add_chauffeur(db=db, chauffeur=chauffeur)


@chauffeur_router.get("/get/all/", response_model=List[Chauffeur])
def get_engin_all(db:Session = Depends(get_db)):
    chauffeurs = reads.get_chauffeur_all(db=db)
    if chauffeurs:
        return chauffeurs
    else:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Chauffeur is empty")


@chauffeur_router.get("/get/chauffeurs/{idChauffeur}", response_model=Chauffeur)
def get_chauffeur_by_id(idChauffeur:int,  db: Session = Depends(get_db)):
    chauffeur = reads.get_chauffeur_by_id(db=db, idChauffeur=idChauffeur)
    if chauffeur:
        return chauffeur
    else:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Chauffeur not found")


@chauffeur_router.get("/get/chauffeurs/codepermanent/{codePermanent}", response_model=Chauffeur)
def get_chauffeur_by_code_permanent(codePermanent:str,  db: Session = Depends(get_db)):
    chauffeur = reads.get_chauffeur_by_code_permanent(db=db, codePermanent=codePermanent)
    if chauffeur:
         return chauffeur
    else:
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Code Permanent not found")


# Mission
mission_router = APIRouter(prefix="/missions", tags=["Missions"])

@mission_router.post("/add/", response_model=Mission)
def create_mission(mission:MissionCreate, db: Session = Depends(get_db)):
    return create.add_mission(db=db, mission=mission)


@mission_router.get("/all", response_model=List[Mission])
def get_all_mission(db:Session = Depends(get_db)):
    return reads.get_mission_all(db=db)

# Partenaire
partenaire_router = APIRouter(prefix="/partenaires", tags=["Partenaires"])

@partenaire_router.post("/add", response_model=Partenaire)
def create_partenaire(partenaire: PartenaireCreate, db: Session = Depends(get_db)):
    return create.add_partenaire(db=db, partenaire=partenaire)

app = FastAPI(debug=True, title="OptiDrive")
app.include_router(engin_router)
app.include_router(chauffeur_router)
app.include_router(partenaire_router)
app.include_router(mission_router)
