import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

dp = Dispatcher()
api =''
bot = Bot(token=api)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('start'))
async def start_command(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')
    
@dp.message(F.text == 'Calories')
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
