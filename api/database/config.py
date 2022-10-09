from venv import create
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db", echo=True)

base = declarative_base()

session = sessionmaker(bind=engine)