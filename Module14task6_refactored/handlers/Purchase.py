from aiogram import types

import Module14task6_refactored.database as database
from Module14task6_refactored.database import get_all_products
from Module14task6_refactored.keyboards import kb3
# from main import prods


async def get_buying_list(message: types.Message):
    for item in database.get_all_products():
        await message.answer(text=f'Название: {item[1]}|Описание: {item[2]}|Цена: {item[3]}')
        try:
            photo = types.FSInputFile(f'Module14task3_{item[0]}.jpg')
            await message.answer_photo(photo=photo)
        except:
            await message.answer(f'Фотография {item[1]} будет скоро загружена')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)



async def send_confirm_message(callback: types.CallbackQuery):
    await callback.message.answer('Вы успешно приобрели продукт!')
