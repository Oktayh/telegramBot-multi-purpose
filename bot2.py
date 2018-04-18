import json
import requests

from pprint import pprint

def sendMessage(text,chatid):
    url = "https://api.telegram.org/<token>"
    mes = 'sendMessage?chat_id='+str(chatid)+'&text='+text
    url += mes
    requests.get(url)

update_id=0

while True:
    url = "https://api.telegram.org/<token>"
    Telegram = requests.get(url+"getUpdates")
    TelegramData = Telegram.json()
    
    count = 1
    for i in TelegramData["result"]:
        realLastID = (TelegramData["result"][-1]["update_id"])
        lastId = (TelegramData["result"][count]["update_id"])
        print(lastId)
        count = count + 1

        if realLastID == lastId:
            break
    break

