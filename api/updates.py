from sqlalchemy.orm import Session
from schemas.Engin import EnginChauffeurUpdate
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

