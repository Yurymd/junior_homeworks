import requests
from config import root_url, ok_codes, updates_endpoint, send_message_endpoint, token

class TgBoot():
    def __init__(self, token):
        self.token = token

    def get_updates(self):
        result = {'error': False, 'value': None}
        url = f'{root_url}{self.token}{updates_endpoint}'
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

    def send_message(self, chat_id, text):
        payload = {'chat_id': chat_id, 'text': text}
        url = f'{root_url}{self.token}{send_message_endpoint}'
        res = requests.post(f'{root_url}{self.token}{send_message_endpoint}', data=payload)
        status_code = res.status_code
        if status_code in ok_codes:
            print("200 ok")
        else:
            print(f"Request to {url} failed with status code = {status_code}")

    def process_message(self,text,chat_id):
        if text == "start":
            self.send_message(chat_id, "test")
        else:
            self.send_message(chat_id, "ошибка")

    def process_messages(self):
        last_message_id = 0
        while True:
            if self.get_updates()['error'] == False:
                lastMessage = self.get_updates()['value'][-1]
                text = lastMessage.get('message').get('text')
                chat_id = lastMessage.get('message').get('chat').get('id')
                message_id = lastMessage.get('message').get("message_id")
                if last_message_id < message_id:
                    self.process_message(text,chat_id)
                    last_message_id = message_id

rrr = TgBoot(token).process_messages()
print(rrr)


# def echo(updates, token):
# 	if updates['error'] == False:
# 		updates = updates['value']
# 		last_update = updates[-1]
# 		message = last_update.get('message')
# 		text = message.get('text')
# 		chat_id = message.get('chat').get('id')
# 		send_message(chat_id, text, token)
#
# def send_echo(token):
# 	res = get_updates(token)
# 	echo(res, token)

