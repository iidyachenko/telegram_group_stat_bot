import configparser

from pyrogram import Client

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = int(config["Telegram"]["api_id"])
api_hash = config["Telegram"]["api_hash"]
username = config["Telegram"]["username"]

app = Client(name=username, api_hash=api_hash, api_id=api_id)

with app:
    app.send_message("me", "Это я бот 2")
