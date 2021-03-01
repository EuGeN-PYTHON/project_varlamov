'''
1) переводчик слов
2) * регистр ввода и вывода
'''

def num_translate(num):
    for key, val in num.items():
        if user_word.lower() == key:
            return val.capitalize()
        elif user_word.lower() == val:
            return key.capitalize()
    else:
        return None

numbers_dic = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
user_word = input('Please, enter a number in English or Russian from 0 to 10: ')
print(num_translate(numbers_dic))

'''
3) Словарь имен по буквам
4) *  
'''
# 3 задача

def thesaurus(*args):
    for item in args:
        letter_dic.setdefault(item[0], list(filter(lambda x: x.startswith(item[0]), args)))

        # letter_dic.setdefault(item[0], [item])
        # for key in letter_dic.keys():
        #     if key == item[0] and [item] != letter_dic[key]:
        #         letter_dic[key].append(item)



letter_dic = {}

thesaurus("Иван", "Мария", "Петр", "Илья", "Макс", "Понтий", 'Лена', "Марго")
print(letter_dic)

# 4 Задача


def thesaurus_adv(*args):
    for n_s in args:
        letter_dic_adv.setdefault(n_s[:n_s.index(" "):-1][-1], {})# создаем поочередно словрь по первой букве фамилии
        if not n_s[0] in letter_dic_adv[n_s[:n_s.index(" "):-1][-1]]: # проверяем наличие и добавляем в словарь имя_фамилию иттерируя по аргументам (имени фамилии)
            letter_dic_adv[n_s[:n_s.index(" "):-1][-1]][n_s[0]] = list(filter(
                lambda x: x[:x.index(" "):-1].endswith(n_s[:n_s.index(" "):-1][-1])
                          and x.startswith(n_s[0]), args)
            )
    return letter_dic_adv


letter_dic_adv = {}

thesaurus_adv("Иван Степанов", "Мария Иванова", "Петр Суриков", "Илья Макаров", "Макс Ибрагимов", "Понтий Сукачев", 'Ирина Матросова', "Марго Саркисян")

print(letter_dic_adv)

for sur, n in sorted(letter_dic_adv.items()):  # сортировка

    print(sur)

    for key, item in sorted(n.items()):

        print(f'  {key}: {sorted(item)}')


'''
5) Возврат n шуток 
'''

from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



def get_jokes(n, m = 1):
    for i in range(n):
        nouns_i = nouns[randrange(len(nouns))]
        adverbs_i = adverbs[randrange(len(adverbs))]
        adjectives_i = adjectives[randrange(len(adjectives))]
        print(f'{nouns_i} {adverbs_i} {adjectives_i}')
        if m == 0:
            nouns.remove(nouns_i)
            adverbs.remove(adverbs_i)
            adjectives.remove(adjectives_i)


n = int(input(f'Введите количество шуток от 1 до {len(nouns)}:  '))
m = int(input('Введите 0, если хотите исключить повторяющиеся слова в шутках:  '))

get_jokes(n, m)# 1 - аргумент количество шуток, 2 - аргумент разрешает (1), или запрещает (0) повторный вывод слов.
