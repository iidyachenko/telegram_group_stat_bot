import asyncio
import configparser
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")
bot = Bot(token=config["Telegram"]["bot_token"])

dp = Dispatcher(bot)


# Обработчик команды /start
@dp.message_handler(Command("start"))
async def get_chat_members(message: types.Message):
    await message.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@dp.message_handler()
async def message_handler(message: types.Message):
    await message.answer(f"Твой ID: {message.from_user.id}")


async def main():
    # Стартуем бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
