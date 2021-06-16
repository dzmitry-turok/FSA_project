import os
import pytest
from alembic import command
from alembic.config import Config
from app.db import database
from sqlalchemy_utils import create_database, drop_database

os.environ['TESTING'] = 'True'


@pytest.fixture(scope="module")
def temp_db():
    """ Create tests database """
    print(database.DATABASE_URL)
    database.get_database_url()
    create_database(database.get_database_url())

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")

    try:
        yield database.get_database_url()
    finally:
        drop_database(database.get_database_url())
