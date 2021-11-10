import requests
token = ''
root_url = 'https://api.telegram.org/bot'
updates_endpoint = '/getUpdates'
send_message_endpoint = '/sendMessage'

ok_codes = (200,201,202,203,204,205)

def get_updates(token):
	result = {'error': False, 'value': None}
	url = f'{root_url}{token}{updates_endpoint}'
	res = requests.get(url)
	status_code = res.status_code
	if status_code in ok_codes:
		updates = res.json().get('result')
		result['value'] = updates
		return result
	else:
		error_message = f'Request failed with status code {status_code}'
		print(error_message)
		result['error'] = True
		return result

def send_message(chat_id, text):
	payload = {'chat_id': chat_id, 'text': text}
	url = f'{root_url}{token}{send_message_endpoint}'
	res = requests.post(f'{root_url}{token}{send_message_endpoint}', data=payload)
	status_code = res.status_code
	if status_code in ok_codes:
		print("200 ok")
	else:
		print(f"Request to {url} failed with status code = {status_code}")

def echo(updates):
	if updates['error'] == False:
		updates = updates['value']
		last_update = updates[-1]
		message = last_update.get('message')
		text = message.get('text')
		chat_id = message.get('chat').get('id')
		send_message(chat_id, text)

def send_echo(token):
	res = get_updates(token)
	echo(res)
send_echo(token)



# usd_to_byn_today = requests.get('https://www.nbrb.by/api/exrates/rates/431').json().get('Cur_OfficialRate')

# start_answer = '/start запускает бота и выдает вам список команд \n/hello это приветсвие, бот поздоровается с вами \n/kurs на сегодня выведет вам список курсов валют'
# hello_answer = 'Вітаю'
# kurs_answer = f'Курс доллара на сегодня по нацбанку: {usd_to_byn_today}'

# def choose_answer():
# 	if last_message_text == '/start':
# 		return start_answer
# 	if last_message_text == '/hello':
# 		return hello_answer
# 	if last_message_text == '/kurs':
# 		return kurs_answer
# 	if last_message_text == 'Жыве Беларусь':
# 		return 'Жыве!'
# 	else:
# 		return 'net otveta' 
		
# response_message = choose_answer()
# post_response = requests.post(f'{api_url}{token}{api_send_message}?chat_id={chat_id}&text={response_message}')