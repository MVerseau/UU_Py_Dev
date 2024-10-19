from aiogram import types
from aiogram.fsm.state import StatesGroup, State

import keyboards
from database import is_included, add_user

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000
async def sign_up(message: types.Message, state):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await state.set_state(RegistrationState.username)


async def set_username(message, state):
    if is_included(message.text) == True:
        await message.answer('Пользователь с таким именем уже существует, введите другое имя')
        await state.set_state(RegistrationState.username)
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await state.set_state(RegistrationState.email)


async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:', reply_markup=keyboards.kb)
    await state.set_state(RegistrationState.age)


async def set_age(message, state):
    await state.update_data(age=message.text)
    new_user = await state.get_data()
    add_user(new_user['username'], new_user['email'], new_user['age'])
    await state.clear()
