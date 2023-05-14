import configparser

from pyrogram import Client
from pyrogram.types import Message

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = int(config["Telegram"]["api_id"])
api_hash = config["Telegram"]["api_hash"]
username = config["Telegram"]["username"]
bot_name = config["Telegram"]["bot_name"]
bot_token = config["Telegram"]["bot_token"]

bot_app = Client(name=bot_name, api_hash=api_hash, api_id=api_id, bot_token=bot_token)

@bot_app.on_message()
async def echo(client: Client, message: Message):
    chat = await client.get_me()
    print(chat)
    await message.reply(message.text)

print("Начало работы бота")
bot_app.run()
