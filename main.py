import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6911865322:AAHKOcmdQCQIaN7lwTORikSXJhs9_QOVKqs'
CAT_URL = 'https://random.dog/woof.json'
ERROR_TEXT = 'Здесь должно быть фото собаки.'

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str
timeout = 100

while counter < 100:

	print('attempt =', counter)


	updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
	print(updates)

	if updates['result']:
		for result in updates['result']:
			offset = result['update_id']
			chat_id = result['message']['from']['id']
			cat_response = requests.get(f'{CAT_URL}')
			if cat_response.status_code == 200:
				cat_link = cat_response.json()['url']
				requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
			else:
				requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

	time.sleep(1)
	counter += 1