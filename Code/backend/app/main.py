from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from .database import Album_SessionLocal, Bands_SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models
from typing import List
from . import schemas
from . import CRUD
from pydantic import ValidationError


def get_db_album():
    db = Album_SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db_bands():
    db = Bands_SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
def get_albums(db: Session = Depends(get_db_album)):
    return CRUD.get_albums(db)


@app.get(
    "/bands/",
    response_model=List[schemas.ReadBand],
    responses={
        404: {"model": schemas.MessageNotFound, "description": "The item was not found"}
    },
)
def get_bands(db: Session = Depends(get_db_bands)):
    try:
        bands = CRUD.get_bands(db=db)
        if not bands:
            return JSONResponse(status_code=404, content={"message": "liste leer"})
        return bands
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database Server Error",
        ) from e


@app.get(
    "/bands/{band_id}",
    response_model=schemas.ReadBand,
    responses={
        404: {"model": schemas.MessageNotFound, "description": "The item was not found"}
    },
)
def get_bands_id(band_id: int, db: Session = Depends(get_db_bands)):
    try:
        band = CRUD.get_band(band_id, db=db)
        if not band:
            return JSONResponse(
                status_code=404, content={"message": "Keine Band gefunden"}
            )
        return band
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database Server Error",
        ) from e


@app.post("/bands/", response_model=schemas.BandBase)
def post_bands(band: schemas.BandCreate, db: Session = Depends(get_db_bands)):
    try:
        new_band = CRUD.post_band(db=db, band=band)
        return new_band
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from e
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# docker-compose down
# docker-compose build --no-cache
# docker-compose up
