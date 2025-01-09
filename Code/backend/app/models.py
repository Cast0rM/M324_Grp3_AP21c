from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DECIMAL,
    TIMESTAMP,
    ForeignKey,
    DateTime,
    CheckConstraint,
)
from sqlalchemy.sql import func
from sqlalchemy.sql.functions import now
from .database import Album_Base, Bands_Base


class Album(Album_Base):
    __tablename__ = "albums"

    album_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    release_date = Column(Date, nullable=False)
    band_id = Column(Integer, nullable=False)
    label = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class Bands(Bands_Base):
    __tablename__ = "bands"
    band_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=False)
    founding_date = Column(Date, nullable=False)
    members_count = Column(Integer, nullable=False)
    disbanded_date = Column(String(10), default=None, nullable=True)
    created_at = Column(DateTime, default=now())

    # __table_args__ = (
    #     CheckConstraint(
    #         "disbanded_date IS NULL OR disbanded_date > founding_date",
    #         name="check_disbanded_after_founding"
    #     ),
    # )


# class Bands(Bands_Base)


# Base.metadata.create_all()
