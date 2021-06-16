from sqlalchemy import Column, Integer, String
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select
from sqlalchemy import delete as sqlalchemy_delete

from app.db.database import Base, async_db_session


class CrudModel:
    @classmethod
    async def create(cls, **kwargs):
        async_db_session.add(cls(**kwargs))
        await async_db_session.commit()

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
            .where(cls.id == int(id))
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def get(cls, id):
        query = select(cls).where(cls.id == id)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result

    @classmethod
    async def get_all_record(cls):
        query = select(cls)
        results = await async_db_session.execute(query)
        return results.scalars().all()

    @classmethod
    async def get_by_email(cls, email):
        query = select(cls).where(cls.email == email)
        results = await async_db_session.execute(query)
        return results.scalars().all()

    @classmethod
    async def delete(cls, id):
        query = (
            sqlalchemy_delete(cls)
            .where(cls.id == int(id))
        )
        await async_db_session.execute(query)
        await async_db_session.commit()


class User(Base, CrudModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
