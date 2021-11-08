import requests
token = '2122464959:AAGTAzbUVlVerMMlDXaYbpgC0F8tiIdcaig'
api_url = 'https://api.telegram.org/bot'
api_update = '/getUpdates'
api_send_message = '/sendMessage'

update_message = requests.get(api_url+token+api_update)
last_message = update_message.json().get('result')[-1].get('message').get('text')
last_chat_id = update_message.json().get('result')[-1].get('message').get('chat').get('id')
usd_to_byn_today = requests.get('https://www.nbrb.by/api/exrates/rates/431').json().get('Cur_OfficialRate')

start_answer = '/start запускает бота и выдает вам список команд \n/hello это приветсвие, бот поздоровается с вами \n/kurs на сегодня выведет вам список курсов валют'
hello_answer = 'Вітаю'
kurs_answer = f'Курс доллара на сегодня по нацбанку: {usd_to_byn_today}'

def choose_answer():
	if last_message == '/start':
		return start_answer
	if last_message == '/hello':
		return hello_answer
	if last_message == '/kurs':
		return kurs_answer
	if last_message == 'Жыве Беларусь':
		return 'Жыве!'
	else:
		return 'net otveta' 
response_message = choose_answer()
post_response = requests.post(f'{api_url}{token}{api_send_message}?chat_id={last_chat_id}&text={response_message}')