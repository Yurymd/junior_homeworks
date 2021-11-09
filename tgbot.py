import requests
token = ''
root_url = 'https://api.telegram.org/bot'
updates_endpoint = '/getUpdates'
send_message_endpoint = '/sendMessage'


# last_message = updates.json().get('result')[-1].get('message')
# last_message_text = last_message.get('text')
# chat_id = last_message.get('chat').get('id')

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

result = get_updates(token)
if result['error'] == False:
	updates = result['value']
	last_update = updates[-1]
	message = last_update.get('message')
	last_message = message.get('text')
	print(last_message)


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