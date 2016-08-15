from . import secrets
import json
from pprint import pprint
import requests

base= "https://api.telegram.org/bot"+secrets.token+"/"

def get(command):
    r=requests.get(base+command)
    return json.loads(r.text)

def echo(msg):
    data = json.loads(msg)
    with open('new.txt', 'a') as f:
        f.write(msg)
        f.write('\n---------------------------------------------------------\n\n\n')
    user_id = data['result'][0]['message']['from']['id']
    reply = "This is my reply."
    send_msg = get('sendmessage?text='+reply+'&chat_id='+str(user_id))

