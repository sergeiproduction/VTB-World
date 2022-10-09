from pydantic import BaseModel

class TeammateORM(BaseModel):
    team_id: int
    user_id: int

    class Config:
        orm_mode = True