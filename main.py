#!/usr/bin/python3
import json
import requests
from func import *

Creds = open("creds").readline()
TOKEN = str(Creds).strip()

BASE = "https://api.telegram.org/"


def main():

    TELEGRAM = requests.get(BASE+"bot"+TOKEN+"/getUpdates").json()
    LASTRES = len(TELEGRAM["result"])-1
    LASTREPLIED = LASTRES -1 ## For testing delete me

    while True:
        TELEGRAM = requests.get(BASE+"bot"+TOKEN+"/getUpdates").json()
        LASTRES = len(TELEGRAM["result"])-1

        if LASTRES == LASTREPLIED:
            continue
        else:
            LASTREPLIED += 1

            update_id                = TELEGRAM["result"][LASTREPLIED]["update_id"]

            message                  = TELEGRAM["result"][LASTREPLIED].get("message")
            if message != None:
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

                Photo                    = message.get("photo")
                if Photo != None:
                    file_id              = Photo[-1]["file_id"]

                messageDocument              = message.get("document")
                if messageDocument != None:
                    mime_type                = messageDocument["mime_type"]
                    fileName                 = messageDocument["file_name"]
                    file_id                  = messageDocument["file_id"]
                    file_size                = messageDocument["file_size"]

                Contact                  = message.get("contact")
                if Contact != None:
                    first_name                     = Contact["first_name"]
                    last_name                      = Contact["last_name"]
                    phone_number                   = Contact["phone_number"]
                    user_id                        = Contact["user_id"]

            date                     = message["date"]
            caption                  = message.get("caption")
            text                     = message.get("text")

            if text is not None:
                sendMessage(messageChatId,"Hello, "+messageFromFirst_name+";\nYou typed: "+text)
            else:
                sendMessage(messageChatId,"Hello, "+messageFromFirst_name)


if __name__ == "__main__":
    main()
