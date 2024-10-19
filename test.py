from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
API_TOKEN = 'Ваш_API_Токен'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.callback_query_handler(lambda c: c.data == 'button1')
@dp.callback_query_handler(lambda c: c.from_user.id == 123456)
async def callback_handler(callback: types.CallbackQuery):
    await callback.answer('Вы нажали кнопку 1!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)