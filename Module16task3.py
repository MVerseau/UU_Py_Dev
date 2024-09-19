from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/users/{username}/{age}')
async def new_user(username: Annotated[
    str, Path(min_length=1, max_length=20, description='Enter your username', example='Myname')],
                   age: Annotated[int, Path(ge=18, min_length=2, description='How old are you?', example=20)]) -> str:
    max_index = str(int(max(users, key=int)) + 1)
    users[max_index] = f'Имя: {username}, возраст: {age}'
    return f"User {max_index} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def change_user(user_id: Annotated[int, Path(ge=0, le=int(max(users, key=int)))],
                      username: Annotated[
                          str, Path(min_length=1, max_length=20, description='Enter your username', example='Myname')],
                      age: Annotated[
                          int, Path(ge=18, min_length=2, description='How old are you?', example=20)]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(ge=0, le=int(max(users, key=int)))]) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
