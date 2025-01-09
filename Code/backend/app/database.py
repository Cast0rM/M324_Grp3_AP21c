from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ALBUM_USERNAME = "root"
ALBUM_PASSWORD = "password"
ALBUM_HOST = "albums-db"
ALBUM_PORT = 3306
ALBUM_DATABASE = "albums_db"

BANDS_USERNAME = "root"
BANDS_PASSWORD = "password"
BANDS_HOST = "bands-db"
BANDS_PORT = 3306
BANDS_DATABASE = "bands_db"

# Corrected connection string
connect_string_albums = f"mysql+pymysql://{ALBUM_USERNAME}:{ALBUM_PASSWORD}@{ALBUM_HOST}:{ALBUM_PORT}/{ALBUM_DATABASE}?charset=utf8"


# Corrected connection string
connect_string_bands = f"mysql+pymysql://{BANDS_USERNAME}:{BANDS_PASSWORD}@{BANDS_HOST}:{BANDS_PORT}/{BANDS_DATABASE}?charset=utf8"

album_engine = create_engine(connect_string_albums)

bands_engine = create_engine(connect_string_bands)

Album_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=album_engine)
Bands_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=bands_engine)

Album_Base = declarative_base()
Bands_Base = declarative_base()
