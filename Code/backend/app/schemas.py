from pydantic import BaseModel
from datetime import date, datetime
from typing import List


class Albumbase(BaseModel):
    title: str
    release_date: date
    band_id: int
    label: str
    price: float
    created_at: datetime

class BandBase(BaseModel):
    band_id: int
    name: str
    genre: str
    founding_date: date
    members_count: int
    disbanded_date: str = None
    created_at: datetime
    


class MessageNotFound(BaseModel):
    message: str