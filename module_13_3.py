from aiogram import  Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import  MemoryStorage
import asyncio
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text = ['Urban' , 'ff'])
async def urban_message(message):
    print("Urban message!")
    await message.answer("Вы написали Urban или ff!")

@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Start message!")
    await message.answer("Привет! Я бот, следящий за твоим здоровьем!")

@dp.message_handler()
async def all_message(message):
    print("Получено сообщение!")
    await message.answer("Введите  /start , чтобы начать общение!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)   #  Эта строка запускает бота
    # и начинает получать обновления из Telegram
