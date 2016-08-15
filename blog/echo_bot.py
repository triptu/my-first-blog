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
    with open('new.txt', 'w') as f:
        f.write(msg)
        f.write('\n---------------------------------------------------------\n\n\n')
    user_id = data['message']['from']['id']
    f_name = data['message']['from']['first_name']
    user_msg = data['message']['text']
    with open('new.txt', 'a') as f:
        f.write('User name-%s\n' %f_name)
        f.write('message- %s' %user_msg)
    reply = user_msg
    send_msg = get('sendmessage?text='+reply+'&chat_id='+str(user_id))

