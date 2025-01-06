from sqlalchemy.orm import Session  # Importing Session from SQLAlchemy to manage database transactions
from . import models  # Importing model to access database models and schemas


def get_albums(db: Session):
    return db.query(models.Album).all()

def get_bands(db: Session):
    return db.query(models.Bands).all()