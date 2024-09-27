from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from Module17task5.backend.db_depends import get_db
from typing import Annotated
from Module17task5.models import User, Task
from Module17task5.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(get_db: Annotated[Session, Depends(get_db)]):
    all_users = get_db.scalars(select(User)).all()
    return all_users


@router.get('/user_id')
async def user_by_id(get_db: Annotated[Session, Depends(get_db)], user_id: int):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    return user


@router.post('/create')
async def create_user(get_db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    get_db.execute(insert(User).values(username=create_user.username, firstname=create_user.firstname,
                                       lastname=create_user.lastname, age=create_user.age,
                                       slug=slugify(create_user.username)))
    get_db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(get_db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    get_db.execute(
        update(User).where(User.id == user_id).values(firstname=update_user.firstname,
                                                      lastname=update_user.lastname, age=update_user.age))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_user(get_db: Annotated[Session, Depends(get_db)], user_id: int):
    user = get_db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    get_db.execute(delete(User).where(User.id == user_id))
    get_db.execute(delete(Task).where(Task.user_id == user_id))
    get_db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User deleted is successful!'}
