import configparser

from pyrogram import Client, filters

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = int(config["Telegram"]["api_id"])
api_hash = config["Telegram"]["api_hash"]
username = config["Telegram"]["username"]
bot_name = config["Telegram"]["bot_name"]

app = Client(name=username, api_hash=api_hash, api_id=api_id)


@app.on_message()
async def my_handler(client, message):
    print(message)


async def main():
    async with app:
        # Send a message, Markdown is enabled by default
        print("Начало работы клиента")
        async for dialog in app.get_dialogs(limit=10):
            print(dialog.chat.first_name or dialog.chat.title)
        print("End работы клиента")

print("Client start")
app.run()
