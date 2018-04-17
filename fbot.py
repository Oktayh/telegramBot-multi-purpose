import json
import requests

from pprint import pprint

def sendMessage(text,chatid):
    url = "https://api.telegram.org/bot<token>/"
    mes = 'sendMessage?chat_id='+str(chatid)+'&text='+text
    url += mes
    requests.get(url)

oldMesaj = ""

while True:

    url = "https://api.telegram.org/bot<token>/"
    Telegram = requests.get(url+"getUpdates")
    TelegramData = Telegram.json()
    chatid = (TelegramData["result"][-1]["message"]["chat"]["id"])
    mesaj =  (TelegramData["result"][-1]["message"]["text"])

    if oldMesaj != mesaj:
        sendMessage(mesaj,chatid)
        oldMesaj = mesaj
    
