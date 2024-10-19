from aiogram import types
from aiogram.filters.state import State, StatesGroup

import keyboards
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


async def formula(callback: types.CallbackQuery):
    await callback.message.answer(f'10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


async def set_age(callback: types.CallbackQuery, state):
    await callback.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await state.set_state(UserState.growth)

async def set_weigth(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)

async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f'{10 * int(data['weight']) + 6 * int(data['growth']) - 5 * int(data['age']) - 161}', reply_markup=keyboards.kb)
    await state.clear()

