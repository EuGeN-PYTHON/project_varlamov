import re
import functools

"""
1. Функция парсинга e-mail
"""

RE_DATE = re.compile(r'(?P<username>(?:\w+)[._-]*(?:\w+))@(?P<domain>(?:\w+[.])\w+)')

def pars_mail(name):
    try:
        print(RE_DATE.match(name).groupdict())
    except AttributeError:
        raise ValueError(f'wrong email: {name}')


mail_1 = 'someone@geekbrains.ru'

pars_mail(mail_1)

mail_2 = '123_b@geekbrainsru'

# pars_mail(mail_2)

"""
2* Регулярное выражение для nginx_logs.txt

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] 
"GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

"""


RE_DATE = re.compile('(?P<request_addr>(?:\d{2,}[.]){3}\d+)(?:\s*[-]){2}\s*\[(?P<request_datatime>[^]]+)'
                     '\]\s*"(?P<requested_type>\w{3})\s*(?P<requested_resource>\/\w+\/\w+)'
                     '\s*\w+\/\d+[.]\d"\s*(?P<response_code>\d+)\s(?P<response_size>\d+)\s')
with open("nginx_logs.txt", "r", encoding='utf-8') as f:
    for line in f:
        print(line)
        print(RE_DATE.findall(line))
        break

"""
3. Декоратор
Тип вводимых данных
"""

def type_logger(func):
    @functools.wraps(func)
    def wrapper(args):
        return f'{func.__name__}({args}: {type(args)})'
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)

"""
4.	Написать декоратор с аргументом-функцией (callback), 
позволяющий валидировать входные значения функции 
и выбрасывать исключение ValueError, если что-то не так

"""

def val_checker(lam_func):
    def func_cube(func):
        @functools.wraps(func)
        def wrapper(args):
            if lam_func(args) == True:
                print(func(args))
            if lam_func(args) == False:
                raise ValueError(f"wrong val: {args}")
        return wrapper
    return func_cube


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

calc_cube(5)
# calc_cube(-5)