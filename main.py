#!/usr/bin/python3
import json
import requests
from func import *

TOKEN = open("creds").readline()
URL=str(TOKEN).strip()

TELEGRAM = requests.get(URL+"getUpdates").json()
LASTRES = len(TELEGRAM["result"])-1
LASTREPLIED = LASTRES

while True:

    TELEGRAM = requests.get(URL+"getUpdates").json()
    LASTRES = len(TELEGRAM["result"])-1

    if LASTRES == LASTREPLIED:
        continue
    else:
        LASTREPLIED +=1

        update_id                = TELEGRAM["result"][LASTREPLIED]["update_id"]

        message                  = TELEGRAM["result"][LASTREPLIED]["message"]
        message_id               = message["message_id"]

        messageFrom              = message["from"]
        messageFromId            = messageFrom["id"]
        messageFromIs_bot        = messageFrom["is_bot"]
        messageFromFirst_name    = messageFrom["first_name"]
        messageFromUsername      = messageFrom["username"]
        messageFromLanguage_code = messageFrom["language_code"]

        messageChat              = message["chat"]
        messageChatId            = messageChat["id"]
        messageChatFirst_name    = messageChat["first_name"]
        messageChatUsername      = messageChat["username"]
        messageChatType          = messageChat["type"]

        date                     = message["date"]
        text                     = message["text"]

        print(text)
