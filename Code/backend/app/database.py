from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "password"
MYSQL_HOST = "albums-db"
MYSQL_PORT = 3306
MYSQL_DATABASE = "albums_db"

# Corrected connection string
connect_string = f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8'

engine = create_engine(connect_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
