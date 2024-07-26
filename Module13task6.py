import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

dp = Dispatcher()
api = ''
bot = Bot(token=api)

button_info = types.KeyboardButton(text='Информация')
button_calc = types.KeyboardButton(text='Рассчитать')
kb = types.ReplyKeyboardMarkup(keyboard=[[button_calc, button_info]], resize_keyboard=True)


button_info = types.InlineKeyboardButton(text='Формула расчёта', callback_data='formulae')
button_calc = types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
kb2 = types.InlineKeyboardMarkup(inline_keyboard=[[button_calc, button_info]])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)

@dp.message(F.text=='Рассчитать')
async def main_menu(message:types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query(F.data=='formulae')
async def formula(callback:types.CallbackQuery):
    await callback.message.answer(f'10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')

@dp.callback_query(F.data == 'calories')
async def set_age(callback:types.CallbackQuery, state):
    await callback.message.answer('Введите свой возраст:')
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
