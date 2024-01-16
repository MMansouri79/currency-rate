import requests
import json
from config import url, rules

def get_rate():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))

def send_mail(timestamp, rates):
    subject = f'{timestamp}'
    if rules['currencies'] is not None:
        tmp = dict()
        for currency in rules['currencies']:
            tmp[currency] = rates[currency]

        rates = tmp
    text = json.dumps(rates)


if __name__ == '__main__':
    res = get_rate()

    if rules['archive']:
        archive(res['timestamp'], res['rates'])

    if rules['send_mail']:
        send_mail(res['timestamp'], res['rates'])


