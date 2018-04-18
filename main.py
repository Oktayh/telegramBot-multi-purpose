#!/usr/bin/python3
import json
import requests
from func import *

TOKEN = open("creds").readline()
URL=str(TOKEN).strip()

TELEGRAM = requests.get(URL+"getUpdates").json()
LASTRES = len(TELEGRAM["result"])-1

while True:
    update_id                = TELEGRAM["result"][LASTRES]["update_id"]

    message                  = TELEGRAM["result"][LASTRES]["message"]
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

    sendMessage(messageChatId,"Hello World")

    break
