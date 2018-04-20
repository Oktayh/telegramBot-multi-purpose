import requests

TOKEN = open("creds").readline().strip()
BASE="https://api.telegram.org/"

def sendMessage(chatid,text):
    requests.get(BASE+"bot"+TOKEN+"/sendMessage?chat_id="+str(chatid)+"&text="+text)

def getFile(file_id):
    file_path = requests.get(BASE+"bot"+TOKEN+"/getFile?file_id="+file_id).json()
    file_path = file_path["result"]["file_path"]
    return file_path

def download(file_path):
    r = requests.get(BASE+"file/bot"+TOKEN+"/"+file_path, stream=True)
    with open(file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
