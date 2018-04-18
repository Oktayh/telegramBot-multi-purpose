import requests

TOKEN = open("creds").readline()
URL=str(TOKEN).strip()

def sendMessage(chatid,text):
    requests.get(URL+'sendMessage?chat_id='+str(chatid)+'&text='+text)
