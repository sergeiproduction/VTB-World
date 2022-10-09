from pydantic import BaseModel

class TaskORM(BaseModel):
    name: str
    difficulty_id: int
    award: int
    exp: int
    deadline: int

    class Config:
        orm_mode = True