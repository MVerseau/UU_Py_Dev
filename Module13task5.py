import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

dp = Dispatcher()
api = '7390509811:AAGZ9MzIsp66MgyqTlE52aFIwIACb8WJfbc'
bot = Bot(token=api)

button_info = types.KeyboardButton(text='Информация')
button_calc = types.KeyboardButton(text='Рассчитать')
kb = types.ReplyKeyboardMarkup(keyboard=[[button_calc, button_info]], resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message(F.text == 'Рассчитать')
async def set_age(message, state):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weigth(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f'{10 * int(data['weight']) + 6 * int(data['growth']) - 5 * int(data['age']) - 161}')
    await state.clear()


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
