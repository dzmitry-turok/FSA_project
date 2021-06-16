from sys import modules
import uvicorn
from fastapi import FastAPI
from app.db.database import async_db_session
from app.routers import user_routers

app = FastAPI()


@app.on_event("startup")
async def startup():
    await async_db_session.init()
    await async_db_session.create_all()

app.include_router(user_routers.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8090)
