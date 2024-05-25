from mydb import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models 
from schemas.Engin import EnginCreate, Engin, EnginChauffeur, EnginChauffeurUpdate, EnginCHauffeurCodePermanent
from schemas.Chauffeur import Chauffeur, ChauffeurCreate
from schemas.Mission import Mission, MissionCreate, MissionUpdateFin, MissionResponseUpdate
from schemas.Partenaire import Partenaire, PartenaireCreate
from schemas.RechargeFuel import RechargeFuel, RechargeFuelCreate, RechargeFuelEnginResponse
from schemas.Affecter import Affecter, AffecterCreate
from schemas.Deplacement import Deplacement, DeplacementCreate
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
    return engins
    

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


@engin_router.put("/update/engin/chauffeur/{immatricule}", response_model = EnginChauffeur)
def update_engin_immatricule_code_permanent(immatricule:str, chauffeur:EnginCHauffeurCodePermanent, db:Session=Depends(get_db)):
    updated = updates.update_engin_chauffeur_with_immatricule_code_permanent(db=db, immatricule=immatricule, chauffeur_update=chauffeur)
    if updated:
        return updated
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Error assignation")


@engin_router.put("/update/engin/unassign/{immatricule}", response_model=Engin)
def update_engin_unassign(immatricule:str, db: Session = Depends(get_db)):
    updated = updates.update_engin_unassign_with_immatricule(immatricule=immatricule, db=db)
    if updated:
        return updated
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Engin {immatricule} not found") 


@engin_router.put("/update/engin/unassign/chauffeur/{codePermanent}", response_model=Engin)
def update_engin_unassign_chauffeur(codePermanent:str, db:Session = Depends(get_db)):
    db_chauffeur = reads.get_chauffeur_by_code_permanent(db=db, codePermanent=codePermanent)
    if db_chauffeur:
        updated = updates.update_unassign_chauffeur_engin_with_code_permanent(db=db, codePermanent=codePermanent)
        if updated:
            return updated
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Code Permanent: {codePermanent} Non Engin assign Chauffeur") 
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Code Permanent: {codePermanent} Not Found")



# Chauffeur
chauffeur_router = APIRouter(prefix="/chauffeurs", tags=["Chauffeurs"])

@chauffeur_router.post("/add", response_model=Chauffeur)
def create_chauffeur(chauffeur:ChauffeurCreate, db: Session = Depends(get_db)):
    codePermanent = chauffeur.model_dump()['codePermanent']
    db_code_permanent = reads.get_chauffeur_by_code_permanent(db=db, codePermanent=codePermanent)
    if db_code_permanent:
        raise HTTPException(status_code=404, detail="Code Permanent deja enregistre")
    return create.add_chauffeur(db=db, chauffeur=chauffeur)


@chauffeur_router.get("/get/all/", response_model=List[Engin])
def get_engin_all(db:Session = Depends(get_db)):
    chauffeurs = reads.get_engin_all(db=db)
    return chauffeurs


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


@mission_router.get("/get/all", response_model=List[Mission])
def get_all_mission(db:Session = Depends(get_db)):
    return reads.get_mission_all(db=db)


@mission_router.get("/get/{idMission}", response_model=Mission)
def get_mission_by_id(idMission:int, db: Session = Depends(get_db)):
    db_mission = reads.get_mission_by_id(idMission=idMission, db=db)
    if db_mission:
        return db_mission
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Mission not found") 


@mission_router.put("/update/mission/{idMission}", response_model=MissionResponseUpdate)
def update_mission_end_date(idMission:int, mission_update:MissionUpdateFin, db:Session = Depends(get_db)):
    updated = updates.update_fin_mission(db=db, idMission=idMission, mission_update=mission_update)
    if updated:
        return updated
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Not updated mission not found") 


# Partenaire
partenaire_router = APIRouter(prefix="/partenaires", tags=["Partenaires"])

@partenaire_router.post("/add", response_model=Partenaire)
def create_partenaire(partenaire: PartenaireCreate, db: Session = Depends(get_db)):
    return create.add_partenaire(db=db, partenaire=partenaire)


@partenaire_router.get("/get/all", response_model=List[Partenaire])
def get_all_partenaire(db:Session = Depends(get_db)):
    return reads.get_partenaire_all(db=db)


@partenaire_router.get("/get/partenaires/{idPartenaire}", response_model=Partenaire)
def get_partenaire_by_id(idPartenaire:int, db: Session = Depends(get_db)):
    db_partenaire = reads.get_partenaire_by_id(idPartenaire=idPartenaire, db=db)
    if db_partenaire:
        return db_partenaire
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Partenaire not found") 


@partenaire_router.get("/get/partenaires/missions/{nomPartenaire}", response_model=List[MissionResponseUpdate])
def get_partenaire_missions_by_name_partner(nomPartenaire:str, db:Session = Depends(get_db)):
    return reads.get_partenaire_mission_by_name(db=db, nomPartenaire=nomPartenaire)


recharge_fuel = APIRouter(prefix="/rechargefuel", tags=["Recharge Fuel Carburant"])


@recharge_fuel.post("/add", response_model=RechargeFuel)
def create_recharge_fuel_engin(recharge:RechargeFuelCreate, db:Session = Depends(get_db)):
    db_engin = reads.get_engin_by_id(db=db, idEngin=recharge.idEngin)
    if db_engin:
        return create.add_recharge_fuel(db=db, recharge=recharge)
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail="Engin not found") 


@recharge_fuel.get("/get/lastrecharge", response_model=RechargeFuelEnginResponse)
def get_last_recharge_fuel_engin_by_immatricule(immatricule:str, db:Session = Depends(get_db)):
    db_recharge = reads.get_last_recharge_engin_immatricule(db=db, immatricule=immatricule)
    if db_recharge:
        return db_recharge
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Engin {immatricule} not found") 


@recharge_fuel.get("/get/allrecharge", response_model=List[RechargeFuelEnginResponse])
def get_last_recharge_fuel_engin_by_immatricule(immatricule:str, db:Session = Depends(get_db)):
    db_recharge = reads.get_all_recharge_engin_immatricule(db=db, immatricule=immatricule)
    if db_recharge:
        return db_recharge
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Engin {immatricule} not found") 


affecter_router = APIRouter(prefix="/affectations", tags=["Affecter Engin Mission"])


@affecter_router.post("/add",response_model=Affecter)
def create_affectation_engin_mission(affecter:AffecterCreate, db:Session = Depends(get_db)):
    db_mission = reads.get_mission_by_id(db=db, idMission=affecter.idMission)
    db_engin = reads.get_engin_by_id(db=db, idEngin=affecter.idEngin)
    if db_mission:
        if db_engin:
            return create.add_affecter(db=db, affecter=affecter)
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Engin not found") 
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Mission not found") 


deplacement_router = APIRouter(prefix="/deplacements", tags=["Deplacement"])


@deplacement_router.post("/add", response_model=Deplacement)
def create_deplacement_engin_mission(deplacement:DeplacementCreate, db:Session=Depends(get_db)):
    engin = reads.get_engin_by_id(db=db, idEngin=deplacement.idEngin)
    mission = reads.get_mission_by_id(db=db, idMission=deplacement.idMission)
    if mission:
        if engin:
            return create.add_deplacement(deplacement=deplacement, db=db)
        raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Engin not found") 
    raise HTTPException(status_code=ERROR_NOT_FOUND, detail=f"Mission not found") 


app = FastAPI(debug=True, title="OptiDrive")
app.include_router(engin_router)
app.include_router(recharge_fuel)
app.include_router(chauffeur_router)
app.include_router(partenaire_router)
app.include_router(mission_router)
app.include_router(affecter_router)
app.include_router(deplacement_router)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
