import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

dotenv_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=dotenv_path)

# Access environment variables injected by GitHub Secrets
ALBUM_USERNAME = os.getenv("ALBUM_USERNAME")
ALBUM_PASSWORD = os.getenv("ALBUM_PASSWORD")
ALBUM_HOST = os.getenv("ALBUM_HOST")
ALBUM_PORT = os.getenv("ALBUM_PORT", 3306)  # Default to 3306 if not provided
ALBUM_DATABASE = os.getenv("ALBUM_DATABASE")

BANDS_USERNAME = os.getenv("BANDS_USERNAME")
BANDS_PASSWORD = os.getenv("BANDS_PASSWORD")
BANDS_HOST = os.getenv("BANDS_HOST")
BANDS_PORT = os.getenv("BANDS_PORT", 3306)  # Default to 3306 if not provided
BANDS_DATABASE = os.getenv("BANDS_DATABASE")

# Connection strings using environment variables
connect_string_albums = (
    f"mysql+pymysql://{ALBUM_USERNAME}:{ALBUM_PASSWORD}@"
    f"{ALBUM_HOST}:{ALBUM_PORT}/{ALBUM_DATABASE}?charset=utf8mb4"
)

connect_string_bands = (
    f"mysql+pymysql://{BANDS_USERNAME}:{BANDS_PASSWORD}@"
    f"{BANDS_HOST}:{BANDS_PORT}/{BANDS_DATABASE}?charset=utf8mb4"
)

# Create SQLAlchemy engines
album_engine = create_engine(connect_string_albums)
bands_engine = create_engine(connect_string_bands)

# Create session locals for albums and bands
Album_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=album_engine)
Bands_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=bands_engine)

# Declare base classes
Album_Base = declarative_base()
Bands_Base = declarative_base()
