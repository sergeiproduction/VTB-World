from database.config import base
from sqlalchemy import Integer, String, Column, ForeignKey

class Team(base):

    __tablename__ = 'team'

    id = Column(Integer, primary_key = True)
    name = Column(String(255))
    leader_id = Column(Integer, ForeignKey('user.id'))
    rating = Column(Integer)