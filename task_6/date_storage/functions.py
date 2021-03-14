import json


def add_number(some_data):
    with open('bakery.json', 'r', encoding='utf-8') as f:
        try:
            date_input = json.load(f)
            date_input.append(some_data)
            with open('bakery.json', 'w', encoding='utf-8') as f:
                json.dump(date_input, f)
        except json.decoder.JSONDecodeError:
             date_input = []
             with open('bakery.json', 'w', encoding='utf-8') as f:
                date_input.append(some_data)
                json.dump(date_input, f)


def show_data(a = 0, n = 0):
    with open('bakery.json', 'r', encoding='utf-8') as f:
        date_input = json.load(f)
        a = int(a)
        n = int(n)
        if a == 0 and n == 0:
            for i in range(len(date_input)):
                print(date_input[i])
        elif n == 0:
            for i in range(a, len(date_input)+1):
                print(date_input[i-1])
        else:
            for i in range(a, n+1):
                print(date_input[i-1])

def create_data(val, new_value):
    with open('bakery.json', 'r', encoding='utf-8') as f:
        date_input = json.load(f)
        if val not in date_input:
            date_input.append(new_value)
            with open('bakery.json', 'w', encoding='utf-8') as f:
                json.dump(date_input, f)
        else:
            date_input[date_input.index(val)] = new_value
            with open('bakery.json', 'w', encoding='utf-8') as f:
                json.dump(date_input, f)





