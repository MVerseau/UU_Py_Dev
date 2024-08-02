import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from Module14task4_crud_functions import *

dp = Dispatcher()
api = '7390509811:AAGZ9MzIsp66MgyqTlE52aFIwIACb8WJfbc'
bot = Bot(token=api)

button_info = types.KeyboardButton(text='Информация')
button_calc = types.KeyboardButton(text='Рассчитать')
button_buy = types.KeyboardButton(text='Купить')
kb = types.ReplyKeyboardMarkup(keyboard=[[button_calc, button_info], [button_buy]], resize_keyboard=True)

inline_button_info = types.InlineKeyboardButton(text='Формула расчёта', callback_data='formulae')
inline_button_calc = types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
kb2 = types.InlineKeyboardMarkup(inline_keyboard=[[inline_button_calc, inline_button_info]])

inline_button_product1 = types.InlineKeyboardButton(text='Product1', callback_data='product_buying')
inline_button_product2 = types.InlineKeyboardButton(text='Product2', callback_data='product_buying')
inline_button_product3 = types.InlineKeyboardButton(text='Product3', callback_data='product_buying')
inline_button_product4 = types.InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3 = types.InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_product1, inline_button_product2, inline_button_product3, inline_button_product4]])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message(F.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query(F.data == 'formulae')
async def formula(callback: types.CallbackQuery):
    await callback.message.answer(f'10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


@dp.callback_query(F.data == 'calories')
async def set_age(callback: types.CallbackQuery, state):
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


@dp.message(F.text == 'Купить')
async def get_buying_list(message: types.Message):
    for item in prods:
        await message.answer(text=f'Название: {item[1]}|Описание: {item[2]}|Цена: {item[3]}')
        try:
            photo = types.FSInputFile(f'Module14task3_{item[0]}.jpg')
            await message.answer_photo(photo=photo)
        except:
            await message.answer(f'Фотография {item[1]} будет скоро загружена')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback: types.CallbackQuery):
    await callback.message.answer('Вы успешно приобрели продукт!')


if __name__ == "__main__":
    initiate_db()
    prods = get_all_products()
    asyncio.run(dp.start_polling(bot))
