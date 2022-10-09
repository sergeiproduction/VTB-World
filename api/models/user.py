from database.config import base
from sqlalchemy import Integer, Column, String, ForeignKey

class User(base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    nickname = Column(String(255))
    role_id = Column(Integer, ForeignKey("role.id"))
    lvl = Column(Integer)