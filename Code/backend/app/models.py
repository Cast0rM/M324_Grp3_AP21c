from sqlalchemy import Column, Integer, String, Date, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class Album(Base):
    __tablename__ = "albums"

    album_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    release_date = Column(Date, nullable=False)
    band_id = Column(Integer, nullable=False)
    label = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    
    
# Base.metadata.create_all()
