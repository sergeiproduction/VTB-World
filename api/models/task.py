from database.config import base
from sqlalchemy import Integer, String, Column, ForeignKey

class Task(base):

    __tablename__ = 'task'

    id = Column(Integer, primary_key = True)
    name = Column(String(255))
    difficulty_id = Column(Integer, ForeignKey('role.id'))
    award = Column(Integer)
    exp = Column(Integer)
    deadline = Column(Integer)