from database.config import base
from sqlalchemy import Integer, String, Column

class Role(base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key = True)
    name = Column(String(255))