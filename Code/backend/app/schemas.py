from pydantic import BaseModel


class Albumbase(BaseModel):
    title: str
    release_date = str
    band_id = int
    label = str
    price = float
    created_at = str

# class BandBase(BaseModel):
#     title: str
#     label: str

# class ItemCreate(BandBase):
#     pass

# class Item(BandBase):
#     id: int

#     class Config:
#         orm_mode = True