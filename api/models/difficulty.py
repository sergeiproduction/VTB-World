from database.config import base
from sqlalchemy import Integer, String, Column

class Difficulty(base):
    __tablename__ = 'difficulty'
    id = Column(Integer, primary_key = True)
    name = Column(String(255))