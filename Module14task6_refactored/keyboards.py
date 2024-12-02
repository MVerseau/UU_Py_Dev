import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command

button_info = types.KeyboardButton(text='Информация')
button_calc = types.KeyboardButton(text='Рассчитать')
button_buy = types.KeyboardButton(text='Купить')
button_registration = types.KeyboardButton(text='Регистрация')
kb = types.ReplyKeyboardMarkup(keyboard=[[button_calc, button_info], [button_buy], [button_registration]],
                               resize_keyboard=True)

inline_button_info = types.InlineKeyboardButton(text='Формула расчёта', callback_data='formulae')
inline_button_calc = types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
kb2 = types.InlineKeyboardMarkup(inline_keyboard=[[inline_button_calc, inline_button_info]])

#FIXME: кнопки по количеству продуктов?
inline_button_product1 = types.InlineKeyboardButton(text='Product1', callback_data='product_buying')
inline_button_product2 = types.InlineKeyboardButton(text='Product2', callback_data='product_buying')
inline_button_product3 = types.InlineKeyboardButton(text='Product3', callback_data='product_buying')
inline_button_product4 = types.InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3 = types.InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_product1, inline_button_product2, inline_button_product3, inline_button_product4]])

