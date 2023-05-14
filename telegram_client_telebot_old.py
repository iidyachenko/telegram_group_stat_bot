import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch, InputPeerEmpty

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest, GetDialogsRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = int(config["Telegram"]["api_id"])
api_hash = config["Telegram"]["api_hash"]
username = config["Telegram"]["username"]

client = TelegramClient(username, api_id, api_hash)

client.start()

chats = []
last_date = None
size_chats = 200
groups = []

result = client(
    GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=size_chats,
        hash=0,
    )
)

chats.extend(result.chats)
for chat in chats:
    try:
        if chat.id == 686046656:
            groups.append(chat)
    except:
        continue

print("Выберите номер группы из перечня:")

for i, g in enumerate(groups):
    print(str(i) + "- " + g.title)

print('Узнаём пользователей...')
all_participants = client.get_participants(groups[0])
for user in all_participants:
    print(user)
