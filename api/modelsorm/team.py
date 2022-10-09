from pydantic import BaseModel

class TeamORM(BaseModel):
    name: str
    leader_id: int
    rating: int

    class Config:
        orm_mode = True