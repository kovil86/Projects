import requests
import time

API_URL = 'http://api.telegram.org/bot' # Адрес API
BOT_TOKEN = '7065946312:AAHQEfhZGkvCjRfXyjCDheLe92WYl170X64' # Токен бота
TEXT = 'Пришел апдейт!'
MAX_COUNTER = 30

offset = -2
counter = 0
chat_id:int

while counter < MAX_COUNTER:
    print('attempt=',counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        print(updates)
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            income_text = result['message']['text']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={income_text}')
    time.sleep(1)
    counter += 1
