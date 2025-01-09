from pydantic import BaseModel
from datetime import date, datetime


class Albumbase(BaseModel):
    title: str
    release_date: date
    band_id: int
    label: str
    price: float
    created_at: datetime


class BandBase(BaseModel):
    name: str
    genre: str
    founding_date: date
    members_count: int
    disbanded_date: str = None


class ReadBand(BandBase):
    band_id: int
    created_at: datetime


class BandCreate(BandBase):
    pass


class MessageNotFound(BaseModel):
    message: str
