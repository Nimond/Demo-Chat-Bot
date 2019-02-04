import requests
import json
import random
from api_key import access_token
from keyboards import default_keyboard, closed_keyboard, empty


access = access_token
id = 176863166
v = '8.92'
admins = [132513584] 
users = []
temp = {
        'blue': 'голубую',
        'white': 'белую',
        'red': 'красную',
        'green': 'зеленую'
        }


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
        print(check)
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
                user_id = update['object']['peer_id']

                params={
                        'user_id': user_id,
                        'v': v, 
                        'access_token': access,                                
                        'random_id': random.randint(0,100000000),
                        'peer_id': user_id
                        }

                if not user_id in users:
                    users.append(user_id)
                    params['keyboard'] = default_keyboard

                if update['object'].get('payload'):
                    payload = json.loads(update['object']['payload'])
                    
                    if not payload['button'] in ['close', 'open', 'close_full']:
                        params['message'] = 'Вы нажали {} кнопку'.format(temp[payload['button']])
                    else:
                        if payload['button'] == 'open':
                            params['keyboard'] = default_keyboard
                            params['message'] = 'открыл'
                        
                        if payload['button'] == 'close':
                            params['keyboard'] = closed_keyboard
                            params['message'] = 'прикрыл'

                        if payload['button'] == 'close_full':
                            # params['keyboard'] = empty
                            params['message'] = 'закрыл'
                else:
                    params['message'] = 'пожалуйста, используйте кнопки'


                r = requests.get('https://api.vk.com/method/messages.send', params=params)

        ts = check['ts']