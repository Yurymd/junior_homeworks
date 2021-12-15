import requests
from config import ok_codes

def currency_by_abbr(abbr):
    url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={abbr}&json'
    try:
        res = requests.get(url)
        status_code = res.status_code

        if status_code in ok_codes:
            body = res.json()
            rate = body[0].get('rate')
            message = f'Курс на сегодня: {rate} грв. за 1 {abbr}'
            return message
        else:
            error_message = f'Request failed with status code {status_code}'
            print(error_message)
    except Exception as e:
        print(e)

