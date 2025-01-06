from fastapi import FastAPI, Depends
from .database import Album_SessionLocal, Bands_SessionLocal
from sqlalchemy.orm import Session
from . import models
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


@app.get("/data")
def get_bands(db: Session = Depends(get_db_bands)):
 return CRUD.get_bands(db)  

# docker-compose down
# docker-compose build --no-cache
# docker-compose up