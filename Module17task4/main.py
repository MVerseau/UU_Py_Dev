from fastapi import FastAPI
from Module17task4.routers import user, task

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}


app.include_router(user.router)
app.include_router(task.router)
