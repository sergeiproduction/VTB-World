from fastapi import FastAPI, status
from database.config import session

from typing import List

from initdb import init_db

from models.user import User
from models.task import Task
from models.team import Team
from models.teammate import Teammate
from models.wallet import Wallet

from modelsorm.teammate import TeammateORM
from modelsorm.user import UserORM
from modelsorm.task import TaskORM
from modelsorm.team import TeamORM
from modelsorm.wallet import WalletORM

import requests 

app = FastAPI()

db = session()

@app.on_event('startup')
def on_startup():
    init_db()



@app.get('/users', response_model=List[UserORM], status_code=status.HTTP_200_OK)
def get_all_users():
    users = db.query(User).all()
    return users

@app.get('/user/{user_id}', response_model=UserORM, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return user

@app.post('/users', response_model=UserORM, status_code=status.HTTP_201_CREATED)
def create_user(user: UserORM):
    user = User(
        name = user.name,
        surname = user.surname,
        nickname = user.nickname,
        role_id = user.role_id,
        lvl = user.lvl
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.put('/user/{user_id}', response_model=UserORM, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UserORM):
    user_updated = db.query(User).filter(User.id == user_id).first()
    user_updated.name = user.name
    user_updated.surname = user.surname
    user_updated.role_id = user.role_id
    user_updated.lvl = user.lvl

    db.commit()
    return user_updated

@app.delete('/user/{user_id}', response_model=UserORM)
def delete_user(user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    db.delete(user)
    db.commit()
    return user



@app.get('/tasks', response_model=List[TaskORM], status_code=status.HTTP_200_OK)
def get_all_users():
    tasks = db.query(Task).all()
    return tasks

@app.post('/tasks', response_model=TaskORM, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskORM):
    task = Task(
        name = task.name,
        difficulty_id = task.difficulty_id,
        award = task.award,
        exp = task.exp,
        deadline = task.deadline
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get('/task/{task_id}', response_model=TaskORM, status_code=status.HTTP_200_OK)
def get_task(task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    return task

@app.put('/task/{task_id}', response_model=TaskORM, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: TaskORM):
    task_updated = db.query(Task).filter(Task.id == task_id).first()
    task_updated.name = task.name
    task_updated.difficulty_id = task.difficulty_id
    task_updated.award = task.award
    task_updated.exp = task.exp
    task_updated.deadline = task.deadline

    db.commit()
    return task_updated

@app.delete('/task/{task_id}', response_model=TaskORM, status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    db.delete(task)
    db.commit()
    return task



@app.get('/teams', response_model=List[TeamORM], status_code=status.HTTP_200_OK)
def get_all_teams():
    teams = db.query(Team).all()
    return teams

@app.post('/team', response_model=TeamORM, status_code=status.HTTP_201_CREATED)
def create_team(team: TeamORM):
    team = Team(
        name = team.name,
        leader_id = team.leader_id,
        rating = team.rating,
    )

    db.add(team)
    db.commit()
    db.refresh(team)
 
    return team

@app.get('/team/{team_id}', response_model=TeamORM, status_code=status.HTTP_200_OK)
def get_team(team_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    return team

@app.put('/team/{team_id}', response_model=TeamORM, status_code=status.HTTP_200_OK)
def update_team(team_id: int, team: TeamORM):
    team_updated = db.query(Team).filter(Team.id == team_id).first()
    team_updated.name = team.name
    team_updated.leader_id = team.leader_id
    team_updated.rating = team.rating
    
    db.commit()
    return team_updated

@app.delete('/team/{team_id}', response_model=TeamORM, status_code=status.HTTP_200_OK)
def delete_team(team_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()

    db.delete(team)
    db.commit()
    return team

@app.get('/teammates/{team_id}', response_model=List[TeammateORM], status_code=status.HTTP_200_OK)
def get_all_teammates(team_id: int):
    teammates = db.query(Teammate).filter(Teammate.team_id == team_id).all()
    return teammates

@app.post('/teammate', response_model=TeammateORM, status_code=status.HTTP_201_CREATED)
def join_team(teammate: TeammateORM):
    
    teammate = Teammate(
        team_id = teammate.team_id,
        user_id = teammate.user_id
    )

    db.add(teammate)
    db.commit()
    db.refresh(teammate)
    return teammate



@app.post("/wallet", response_model=WalletORM, status_code=status.HTTP_201_CREATED)
def create_wallet(wallet: WalletORM):

    api_wallet = requests.post("https://hackathon.lsp.team/hk/v1/wallets/new").json()

    print("WALLET: ", api_wallet)

    wallet = Wallet(        
        public_key = api_wallet['publicKey'],
        private_key = api_wallet['privateKey'],
        matic_balance = wallet.matic_balance,
        ruble_balance = wallet.ruble_balance,  
        nft_balance = wallet.nft_balance,              
        user_id = wallet.user_id
    )


    db.add(wallet)
    db.commit()
    db.refresh(wallet)

    return wallet