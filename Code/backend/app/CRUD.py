from sqlalchemy.orm import (
    Session,
)  # Importing Session from SQLAlchemy to manage database transactions
from . import models  # Importing model to access database models and schemas
from . import schemas
from datetime import datetime


def get_albums(db: Session):
    return db.query(models.Album).all()


def get_bands(db: Session):
    return db.query(models.Bands).all()


def get_band(band_id, db: Session):
    return db.query(models.Bands).filter(models.Bands.band_id == band_id).first()


def post_band(db: Session, band: schemas.BandCreate):
    band_n = models.Bands(
        name=band.name,
        genre=band.genre,
        founding_date=band.founding_date,
        members_count=band.members_count,
        disbanded_date=band.disbanded_date,
        created_at=datetime.now(),
    )
    db.add(band_n)
    db.commit()
    db.refresh(band_n)
    return db.query(models.Bands).order_by(models.Bands.band_id.desc()).first()
