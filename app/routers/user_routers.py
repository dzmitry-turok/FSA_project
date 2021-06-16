from app.schemas import user_schem
from fastapi import APIRouter, HTTPException
from app.models import users

router = APIRouter()


@router.get("/")
async def check_work():
    return {"Check_work": "True"}


@router.get("/all_users")
async def get_all_users():
    user_ids = await users.User.get_all_record()
    return user_ids


@router.post("/create")
async def create_user(user: user_schem.User):
    db_user = await users.User.get_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="A user with this email still exists")
    return await users.User.create(email=user.email)


@router.post("/update")
async def update_user(id, email):
    return await users.User.update(id=id, email=email)


@router.post("/delete")
async def delete_user(id):
    return await users.User.delete(id=id)
