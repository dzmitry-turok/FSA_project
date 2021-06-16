from os import environ
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "localhost")
TESTING = environ.get("TESTING")
DB_NAME = "app_db_test" if TESTING else "app_db"
ASYNC = "" if TESTING else "+asyncpg"


def get_database_url():
    database_url = (f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/app_db_test")
    return database_url

DATABASE_URL = (f"postgresql{ASYNC}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}")

class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def init(self):
        database_url = DATABASE_URL
        self._engine = create_async_engine(database_url, echo=True)
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


async_db_session = AsyncDatabaseSession()
