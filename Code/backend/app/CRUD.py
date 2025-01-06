from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy to manage database transactions
from . import models  # Importing model to access database models and schemas


def get_albums(db: Session):
    return db.query(models.Album).all()

def get_bands(db: Session):
    link_list = []
    link_list =  db.query(models.Bands).all()
    for bands in link_list:
        if bands.disbanded_date == None:
            bands.disbanded_date = "active"
    return link_list