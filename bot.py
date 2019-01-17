import requests
import json
import random
from api_key import access_token
from keyboards import default_keyboard

access = access_token
id = 176863166
v = '8.92'
admins = [132513584] 

def get_longpoll():
    params={
            'group_id': id, 
            'v': v, 
            'access_token': access
            }

    r = requests.get('https://api.vk.com/method/groups.getLongPollServer', params=params)
    return json.loads(r.text)


def check_longpoll(key, server, ts):
    params={
            'act': 'a_check',
            'key': key, 
            'ts': ts, 
            'wait': 25
            }

    r = requests.get(server.replace("\\", ""), params=params)
    return json.loads(r.text)


if __name__ == "__main__":
    first = get_longpoll()
    ts = first['response']['ts']
    server = first['response']['server']
    key = first['response']['key']

    print("ts: {}\nserver: {}\nkey:{}".format(ts, server, key))

    while True:
        check = check_longpoll(key, server, ts)

        if 'failed' in check:
            if check['failed'] == 1:
                ts = check['ts']
            else:
                new = get_longpoll()
                ts = new['response']['ts']
                server = new['response']['server']
                key = new['response']['key']

            continue # if we have error, we have no updates

        for update in check['updates']:
            if update['type'] == 'message_new':
                print("new message: {}, from: {}{}\n".format(
                    update['object']['text'], 
                    update['object']['from_id'] if update['object']['from_id'] not in admins else "admin",
                    "" if not 'payload' in update['object'] else \
                    ", payload: " + json.loads(update['object']['payload'])['button']
                ))

                params={
                        'user_id': update['object']['from_id'],
                        'v': v, 
                        'access_token': access,                                
                        'random_id': random.randint(0,100000000),
                        'message': "na",
                        'peer_id': update['object']['from_id'],
                        'keyboard': default_keyboard
                        }

                r = requests.get('https://api.vk.com/method/messages.send', params=params)

        ts = check['ts']