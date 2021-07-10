
"""
("Dmitii", "Vadim", "Svetlana", "Vadim",'Lena', 'Boris', "Vadim", "Vadim", "Vadim", "Vadim")
Найти индексы всех Вадимов.
"""

some_tuple = ("Dmitii", "Vadim", "Svetlana", "Vadim",'Lena', 'Boris', "Vadim", "Vadim", "Vadim", "Vadim")
some_list = []
i = 1
for el, val in enumerate(some_tuple):
    if val == 'Vadim':
        some_list.append(val + str(i))
        i += 1
    else:
        some_list.append(val)

print(some_list)

some_tuple = ("Dmitii", "Vadim", "Svetlana", "Vadim",'Lena', 'Boris', "Vadim", "Vadim", "Vadim", "Vadim")
some_list = []

for el, val in enumerate(some_tuple):
    some_list.append([el, val])

print(some_list)



some_tuple = ("Dmitii", "Vadim", "Svetlana", "Vadim",'Lena', 'Boris', "Vadim", "Vadim", "Vadim", "Vadim")
for idx in range(len(some_tuple)):
    if some_tuple[idx] == 'Vadim':
         print(f'The name {some_tuple[idx]}  is written under the following index - {idx}')

'''
1.	Выяснить тип результата выражений:
●	15 * 3
●	15 / 3
●	15 // 2
●	15 ** 2

'''

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2

print(type(a))
print(type(b))
print(type(c))
print(type(d))

'''
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
вывести ->
в "05" часов "17" минут температура воздуха была "+05" градусов

* без нового списка
'''

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
some_list_1 = []

for i in some_list:
    if i.isalpha() == True:
        some_list_1.append(i)
    elif i.isdigit() == True:
        i = int(i)
        some_list_1.extend(['"', f'{i:02d}', '"'])
    elif i.isalnum() == False:
        i = int(i)
        some_list_1.extend(['"',f'+{i:02d}', '"'])

print(some_list_1)

some_str = " ".join(some_list_1)
print(some_str)



# Задание под *
# скорее всего это можно было написать +100500 раз корректнее.

temperature = ''
some_str = ''
for i in some_list:
    if i.isdigit() == True:
        i = int(i)
        i = f'"{i:02d}"'
        some_str += i + " "
    elif i.isalnum() == False:
        for n in i:
            if n.isdigit() == False:
                n = f'"{n}'
                temperature += n
            elif n.isdigit() == True:
                n = int(i)
                n = f'{n:02d}"'
                temperature += n
        some_str += temperature + ' '
    else:
        some_str += i + " "

print(some_str)

'''
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Поприветствовать каждого
'''

post_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in post_name:
    i = i[::-1]
    name = i[:i.index(" ")]
    name = name[::-1]
    print(f' Привет, {name.title()}')

'''
СПИСОК ЦЕН
A.	Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).  
B.	Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
C.	Создать новый список, содержащий те же цены, но отсортированные по убыванию.
D.	Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''

price_list = [57.8, 46.51, 97, 10.54, 100.01, 324.1, 23.5, 245.9, 43, 102]

'''
A
'''

price_in_str = ''

for price in price_list:
    price_float = float(price)
    price_str = str(price_float)
    rub, cent = price_str.split('.')
    rub = int(rub)
    cent = int(cent)
    price_in_str += f' {rub} руб. {cent:02d} коп.,'

print(price_in_str)

'''
B
'''

print(id(price_list))
price_list.sort()
print(price_list)
print(id(price_list))

'''
C
'''

new_price_list = list(reversed(price_list))
print(new_price_list)

'''
D
'''
price_list = [57.8, 46.51, 97, 10.54, 100.01, 324.1, 23.5, 245.9, 43, 102]
price_list.sort()
print(sorted(price_list[:len(price_list) - 6:-1]))
