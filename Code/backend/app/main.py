from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from .database import Album_SessionLocal, Bands_SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models
from typing import List
from . import schemas
from . import CRUD


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
    response_model=List[schemas.BandBase],
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


# docker-compose down
# docker-compose build --no-cache
# docker-compose up
