from database.config import base, engine
from models.role import Role
from models.user import User
from models.task import Task
from models.difficulty import Difficulty
from models.team import Team
from models.teammate import Teammate


def init_db():
    print("DATABASE CREATING...")
    base.metadata.create_all(engine)