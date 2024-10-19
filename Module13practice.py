import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from Module13practice_config import *
from Module13practice_keyboards import *
import Module13practice_text
from Module13practice_admin import *
from Module13practice_db import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message):
    await message.answer(Module13practice_text.start,reply_markup=start_kb)

@dp.message(F.text=='О нас')
async def price(message):
    await message.answer(Module13practice_text.about, reply_markup=start_kb)

@dp.message(F.text=='Стоимость')
async def info(message):
    await message.answer('Что вас интересует', reply_markup=catalog_kb)

@dp.callback_query(F.data=='medium')
async def buy_m(callback:types.CallbackQuery):
    await callback.message.answer(Module13practice_text.game_m, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data=='big')
async def buy_l(callback:types.CallbackQuery):
    await callback.message.answer(Module13practice_text.game_l, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data=='mega')
async def buy_xl(callback:types.CallbackQuery):
    await callback.message.answer(Module13practice_text.game_xl, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data=='other')
async def buy_other(callback:types.CallbackQuery):
    await callback.message.answer(Module13practice_text.other, reply_markup=buy_kb)
    await callback.answer()




if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))