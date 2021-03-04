import requests

from datetime import datetime

def currency_rates(name):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content_url = response.text
    date = content_url[content_url.index('Date="'):content_url.index('" name')].replace('Date="', '')
    date = datetime.strptime(date, '%d.%m.%Y').date()
    name = name.upper()
    if name == "USD" or name == "EUR" or name == "GBP" or name == "JPY" or name == "CNY":
        name_from_url = content_url[content_url.index(name):]
        name_from_url = name_from_url[name_from_url.find('<Value>'):name_from_url.index('</Value>'):]
        value = round(float(name_from_url.replace('<Value>', '').replace(',', ".")), 2)
        return f'{value},  {date}'

if __name__ == "__main__":

    name = input('GBP = Фунт стерлингов Соединенного королевства'
             '\nUSD = Доллар США\nEUR = Евро\nCNY = Китайский юань\nJPY = Японских иен\nВведите один из тикеров для получения текущего курса: ')
    print(currency_rates(name))
