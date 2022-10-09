from pydantic import BaseModel

class UserORM(BaseModel):
    name: str
    surname: str
    nickname: str
    role_id: int
    lvl: int

    class Config:
        orm_mode = True