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
    else:
        return None

if __name__ == "__main__":

    name = input('GBP = Фунт стерлингов Соединенного королевства'
             '\nUSD = Доллар США\nEUR = Евро\nCNY = Китайский юань\nJPY = Японских иен\nAUD = Австралийский доллар\n'
                 'AZN = Азербайджанский манат\nAMD = Армянских драмов\nBYN = Белорусский рубль\nBGN = Болгарский лев\nBRL = Бразильский реал\n'
                 'HUF = Венгерских форинтов\nHKD = Гонконгских долларов\nDKK = Датская крона\nINR = Индийских рупий\nKZT = Казахстанских тенге\n'
                 'CAD = Канадский доллар\nKGS = Киргизских сомов\nCNY = Китайский юань\nMDL = Молдавских леев\nNOK = Норвежских крон\n'
                 'PLN = Польский злотый\nRON = Румынский лей\nSGD = Сингапурский доллар\nTJS = Таджикских сомони\nTRY = Турецких лир\n'
                 'TMT = Новый туркменский манат\nUZS = Узбекских сумов\nUAH = Украинских гривен\nCZK = Чешских крон\nSEK = Шведских крон\nCHF = Швейцарский франк\n'
                 'ZAR = Южноафриканских рэндов\nKRW = Вон Республики Корея\nВведите один из тикеров для получения текущего курса: ')
    print(currency_rates(name))
