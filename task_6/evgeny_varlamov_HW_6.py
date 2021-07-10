import sys
import json
import pickle
import itertools
import sys

"""
1.
"""

def get_tuple():
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for i in f:
            contents = i[:i.index('-')] + i[i.index('"'):i.index(' HTTP')].replace('"', '')
            yield tuple(contents.split(" "))

gen_some_list = get_tuple()
print(sys.getsizeof(gen_some_list))

some_list = [i for i in gen_some_list] # Создаем список - условие в ДЗ
print(some_list[0])
print(sys.getsizeof(some_list))

"""
2* Найти Спамера
"""


unique_ip = {some_list[i][0] for i in range(len(some_list))}
many_ip = [some_list[i][0] for i in range(len(some_list))]

count_spamer = 0
dict_ip = {}
for i in unique_ip:
    number_of_input = many_ip.count(i)
    if count_spamer < number_of_input:
        count_spamer = number_of_input
        spamer_ip = i

print(f'Пользователь с IP адрессом: {spamer_ip}, запустил {count_spamer} раз скачивание файлов')

"""
3. Сохранить словарь в файл. Проверить сохранённые данные. 
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. 
Если наоборот — выходим из скрипта с кодом «1».
Оперативная память гораздо больше возможных данных в файлах
"""

new_dict = {}

list_u= []
with open('users.csv', 'r', encoding='utf-8') as f_u:
    for str in f_u:
        list_u.append(str.replace(",", " ").replace('\n',""))

list_h= []
with open('hobby.csv', 'r', encoding='utf-8') as f_h:
    for str in f_h:
        list_h.append(str.replace('\n',""))


for i in range(len(list_u)):
    if len(list_h) > len(list_u):
        print('1')
        break
    elif i >= len(list_h):
        new_dict.setdefault(list_u[i], None)
    else:
        new_dict.setdefault(list_u[i], list_h[i])

print(new_dict)

with open('us_hob.json', 'w+', encoding='utf-8') as f:
    json.dump(new_dict, f)

with open('us_hob.json', 'r', encoding='utf-8') as f:
    new_dict_1 = json.load(f)

print(new_dict_1)

"""
4* users_hobby.txt без словаря
"""
def merge_file_of_str(name_left, name_right, name_final):
    with open(name_left, 'r', encoding='utf-8') as f_users:
        with open(name_right, 'r', encoding='utf-8') as f_hobby:
            with open(name_final, "w", encoding='utf-8') as f_final:
                try:
                    for left, right in itertools.zip_longest(f_users, f_hobby):
                        f_final.write(f'{left.rstrip()}: {right}')
                except AttributeError:
                    sys.exit("Erorr '1': Количество пользователей меньше, чем количество хобби\n"
                             " Файл записан в соответствии с кол-вом пользователей")

if __name__ == "__main__":
    merge_file_of_str("users.csv", "hobby.csv", "final_file.txt")

"""
5** файл для запуска терминала ter_6.py
"""

"""
6 и 7 Реализовано в отдельной директории 'data_storage'
"""
