from fastapi import FastAPI, HTTPException, Request,Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory='templates')

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def new_get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        for user in users:
            if user.id == user_id:
                user_index = users.index(user)

        return templates.TemplateResponse("users.html", {'request': request, "user": users[user_index]})
    except:
        raise HTTPException(status_code=404, detail=f'User was not found')


@app.post('/users/{username}/{age}')
async def new_user(username: str, age: int) -> User:
    user = User(id=len(users) + 1, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def change_user(user_id: int, username: str, age: int) -> User:
    try:

        for user in users:
            if user.id == user_id:
                edit_user = user
                edit_user.username, edit_user.age = username, age

        return edit_user
    except:
        raise HTTPException(status_code=404, detail=f'User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:

        for user in users:
            if user.id == user_id:
                deleted_user = users.pop(users.index(user))
        return deleted_user
    except:
        raise HTTPException(status_code=404, detail=f'User was not found')
