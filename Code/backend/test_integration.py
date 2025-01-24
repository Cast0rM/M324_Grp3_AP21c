import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db_bands
from app.database import Bands_Base

import os

BANDS_USERNAME = os.getenv("BANDS_USERNAME")
BANDS_PASSWORD = os.getenv("BANDS_PASSWORD")
BANDS_HOST = os.getenv("TEST_BANDS_HOST")
BANDS_PORT = os.getenv("BANDS_PORT", 3306)  # Default to 3306 if not provided
BANDS_DATABASE = os.getenv("BANDS_DATABASE")


connect_string_bands = (
    f"mysql+pymysql://{BANDS_USERNAME}:{BANDS_PASSWORD}@"
    f"{BANDS_HOST}:{BANDS_PORT}/{BANDS_DATABASE}?charset=utf8mb4"
)


engine = create_engine(connect_string_bands)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db_album():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_get_db_bands():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db_bands] = override_get_db_bands

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Create tables in the test database
    Bands_Base.metadata.create_all(bind=engine)
    yield
    # Clean up the database after tests
    Bands_Base.metadata.drop_all(bind=engine)


def test_isBandReal():
    response = client.get("/bands/1")
    assert response.status_code == 200
