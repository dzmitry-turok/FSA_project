from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True
