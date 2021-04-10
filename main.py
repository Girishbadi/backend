from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class User(BaseModel):
    user_id = str
    username = "username"
    first_name ="first_name"
    last_name ="last_name"
    email="someone1@example.com"



@app.get('/')
def index():
    return {'key' : 'value'}


@app.get('/Users')
def get_Users():
    return db

@app.get('/Users/{user_id}')
def get_user_by_id(user_id: int):
    return db[user_id-1]

@app.post('/Users')
def create_user(user:User):
    db.append(user.dict())
    return db[-1]

@app.put("/Users/{user_id}")
def update_Users(user_id: str, username: str, first_name: str, last_name: str, email:str):
    results = {"username":username, "user_id": user_id, "first_name": first_name, "last_name": last_name,"email": email}
    return results

@app.delete('/Users/{user_id}')
def delete_user(user_id: int):
    db.pop(user_id-1)
    return{}