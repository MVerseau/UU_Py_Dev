
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/users/{username}/{age}')
async def new_user(username: str, age: int) -> User:
    user = User(id=len(users) + 1, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def change_user(user_id: int, age: int, username: str) -> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username, user.age = username, age
                edit_user=user
        return edit_user
    except:
        raise HTTPException(status_code=404, detail=f'User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:

        for user in users:
            if user.id==user_id:
                deleted_user=users.pop(users.index(user))
        return deleted_user
    except:
        raise HTTPException(status_code=404, detail=f'User was not found')
