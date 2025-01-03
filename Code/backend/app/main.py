from fastapi import FastAPI, Depends
from .database import SessionLocal
from sqlalchemy.orm import Session
from . import models
from . import CRUD

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
def get_albums(db: Session = Depends(get_db)):
 return CRUD.get_albums(db)  


