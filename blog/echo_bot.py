from . import secrets
import json
from pprint import pprint
import requests
from . import bot

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
    results = bot.main(user_msg)
    reply = bot.get(results)
    with open('data\\'+f_name+'-'+str(user_id)+".txt", 'a') as f:
        f.write(user_msg+'\n')
    send_msg = get('sendmessage?text='+reply+'&chat_id='+str(user_id))

