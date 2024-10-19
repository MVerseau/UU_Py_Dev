import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

dp = Dispatcher()
api = '7390509811:AAGZ9MzIsp66MgyqTlE52aFIwIACb8WJfbc'
bot = Bot(token=api)


class UserState(StatesGroup):
    address = State()


@dp.message(Command('start'))
async def buy(message,state):
    await message.answer('Отправьте на свой адрес, пожалуйста.')
    await state.set_state(UserState.address)


@dp.message(UserState.address)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    date = await state.get_data()
    await message.answer(f'Доставка будет отправлена на {date['first']}')
    await state.clear()


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
