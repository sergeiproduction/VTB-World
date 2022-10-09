from database.config import base
from sqlalchemy import Integer, Column, ForeignKey

class Teammate(base):

    __tablename__ = 'teammate'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('team.id'))
    user_id = Column(Integer, ForeignKey('user.id'))