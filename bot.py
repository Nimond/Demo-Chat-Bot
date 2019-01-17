import requests
import json
import random
from basic import get_products


access = 'access token'
id = 176863166
v = '8.92'

def get_longpoll():
    r = requests.get('https://api.vk.com/method/groups.getLongPollServer', params={'group_id': id, 'v': v, 'access_token': access})

    return eval(r.text)


def check_longpoll(key, server, ts):
    r = requests.get(server.replace("\\", ""), params={'act': 'a_check','key': key, 'ts': ts, 'wait': 25})

    return r.text

if __name__ == "__main__":
    first = get_longpoll()
    ts = first['response']['ts']
    server = first['response']['server']
    key = first['response']['key']

    print(ts, server, key)

    while True:
        check = json.loads(check_longpoll(key, server, ts))

        if 'failed' in check:
            if check['failed'] == 1:
                ts = check['ts']
            else:
                new = get_longpoll()
                ts = new['response']['ts']
                server = new['response']['server']
                key = new['response']['key']

            continue # if we have error, we have no updates

        ts = check['ts']

        for update in check['updates']:
            if update['type'] == 'message_new':
                    
                params={
                        'user_id': update['object']['from_id'],
                        'v': v, 
                        'access_token': access,                                
                        'random_id': random.randint(0,100000000),
                        'message': p_message,
                        'peer_id': update['object']['from_id'],
                        }

                requests.get('https://api.vk.com/method/messages.send', params=params)
