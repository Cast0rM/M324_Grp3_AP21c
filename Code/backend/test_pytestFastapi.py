from unittest import mock
import pytest

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
from fastapi.testclient import TestClient
from app.main import app
from app import models


@pytest.fixture
def mock_album_session():
    with mock.patch("sqlalchemy.orm.sessionmaker") as mock_sessionmaker:
        mock_session = mock.Mock()
        mock_sessionmaker.return_value = mock_session
        yield mock_session


@pytest.fixture
def mock_bands_session():
    with mock.patch("sqlalchemy.orm.sessionmaker") as mock_sessionmaker:
        mock_session = mock.Mock()
        mock_sessionmaker.return_value = mock_session
        yield mock_session


@pytest.fixture
def mock_album_engine():
    with mock.patch("sqlalchemy.create_engine") as mock_create_engine:
        mock_engine = mock.Mock()
        mock_create_engine.return_value = mock_engine
        yield mock_engine


@pytest.fixture
def mock_bands_engine():
    with mock.patch("sqlalchemy.create_engine") as mock_create_engine:
        mock_engine = mock.Mock()
        mock_create_engine.return_value = mock_engine
        yield mock_engine


def test_album_session(mock_album_session, mock_album_engine):
    assert mock_album_session is not None
    mock_album_session.execute.assert_not_called()


def test_bands_session(mock_bands_session, mock_bands_engine):
    assert mock_bands_session is not None
    mock_bands_session.execute.assert_not_called()


client = TestClient(app)


def test_read_albums(mock_album_session):
    mock_album_session.query(models.Album).all()

    mock_album_session.query.assert_called_once_with(models.Album)

    mock_album_session.execute.assert_not_called()

    mock_album_session.query().all.return_value = [
        models.Album(album_id=1, title="Test Album", price=10.25)
    ]

    albums = mock_album_session.query(models.Album).all()

    assert len(albums) == 1
    assert albums[0].title == "Test Album"
    assert albums[0].price == 10.25


def test_read_bands(mock_bands_session):
    mock_bands_session.query(models.Bands).all()

    mock_bands_session.query.assert_called_once_with(models.Bands)

    mock_bands_session.execute.assert_not_called()

    mock_bands_session.query().all.return_value = [
        models.Bands(band_id=1, name="Queen", genre="Rock")
    ]

    bands = mock_bands_session.query(models.Bands).all()

    assert len(bands) == 1
    assert bands[0].name == "Queen"
    assert bands[0].genre == "Rock"


def test_get_band_by_id(mock_bands_session):
    band_id = 1
    mock_bands_session.query(models.Bands).filter_by(band_id=band_id).first()
    mock_bands_session.query.assert_called_once_with(models.Bands)
    (mock_bands_session
     .query()
     .filter_by.assert_called_once_with(band_id=band_id)
     )
    mock_bands_session.query().filter_by().first.return_value = models.Bands(
        band_id=1, name="Queen", genre="Rock"
    )
    band = (mock_bands_session
            .query(models.Bands)
            .filter_by(band_id=band_id).first()
            )

    assert band is not None
    assert band.name == "Queen"
    assert band.genre == "Rock"


def test_get_band_by_id_without_band(mock_bands_session):
    band_id = 1
    mock_bands_session.query(models.Bands).filter_by(band_id=band_id).first()
    mock_bands_session.query.assert_called_once_with(models.Bands)
    (mock_bands_session
     .query()
     .filter_by.assert_called_once_with(band_id=band_id)
     )
    mock_bands_session.query().filter_by().first.return_value = models.Bands(
        band_id=1, name="Queen", genre="Rock"
    )
    band = (mock_bands_session
            .query(models.Bands)
            .filter_by(band_id=band_id)
            .first()
            )

    assert band is not None
    assert band.name == "Queen"
    assert band.genre == "Rock"
