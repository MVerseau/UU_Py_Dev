import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command

import handlers.Start
import handlers.Registration
import handlers.Purchase
import handlers.Calculations

from keyboards import *
from config import *
from database import *

dp = Dispatcher()
bot = Bot(token=api)

dp.message(Command('start'))(handlers.Start.start_command)
dp.message(F.text == 'Рассчитать')(handlers.Start.main_menu)

dp.callback_query(F.data == 'formulae')(handlers.Calculations.formula)
dp.callback_query(F.data == 'calories')(handlers.Calculations.set_age)
dp.message(handlers.Calculations.UserState.age)(handlers.Calculations.set_growth)
dp.message(handlers.Calculations.UserState.growth)(handlers.Calculations.set_weigth)
dp.message(handlers.Calculations.UserState.weight)(handlers.Calculations.send_calories)

dp.message(F.text == 'Купить')(handlers.Purchase.get_buying_list)
dp.callback_query(F.data == 'product_buying')(handlers.Purchase.send_confirm_message)

dp.message(F.text == 'Регистрация')(handlers.Registration.sign_up)
dp.message(handlers.Registration.RegistrationState.username)(handlers.Registration.set_username)
dp.message(handlers.Registration.RegistrationState.email)(handlers.Registration.set_email)
dp.message(handlers.Registration.RegistrationState.age)(handlers.Registration.set_age)

if __name__ == "__main__":
    initiate_db()
    asyncio.run(dp.start_polling(bot))
