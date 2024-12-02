from aiogram import types
from keyboards import *

async def start_command(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)

async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

