'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
'''

SEC_IN_MIN = 60
SEC_IN_HOUR = SEC_IN_MIN * 60
SEC_IN_DAY = SEC_IN_HOUR * 24
SEC_IN_MONTH = int(SEC_IN_DAY * ((365*4+1)/(4*12)))
SEC_IN_YEAR = int(SEC_IN_DAY * ((365*4+1)/4))


duration_sec = int(input("Enter the number of seconds: "))
duration = [int(duration_sec // SEC_IN_YEAR), int((duration_sec % SEC_IN_YEAR)) // SEC_IN_MONTH, (duration_sec % SEC_IN_MONTH) // SEC_IN_DAY, (duration_sec % SEC_IN_DAY) // SEC_IN_HOUR, (duration_sec % SEC_IN_HOUR) // SEC_IN_MIN, duration_sec % 60]


while duration[0] > 0 or duration[1] > 0 or duration[2] > 0 or duration[3] > 0 or duration[4] > 0 or duration[5] >= 0:
    duration = [int(duration_sec // SEC_IN_YEAR), int((duration_sec % SEC_IN_YEAR)) // SEC_IN_MONTH, (duration_sec % SEC_IN_MONTH) // SEC_IN_DAY, (duration_sec % SEC_IN_DAY) // SEC_IN_HOUR, (duration_sec % SEC_IN_HOUR) // SEC_IN_MIN, duration_sec % 60]

    if duration[0] != 0:
        print(
            f"Your number of seconds in year(s), month, day(s), hour(s), minute(s) and second(s):{duration[0]} year(s); {duration[1]} month; {duration[2]} day(s);"
            f" {duration[3]} hour(s); {duration[4]} minute(s); {duration[5]} second(s)")
    elif duration[1] != 0:
        print(
            f"Your number of seconds in month, day(s), hour(s), minute(s) and second(s): {duration[1]} month; {duration[2]} day(s);"
            f" {duration[3]} hour(s); {duration[4]} minute(s); {duration[5]} second(s)")
    elif duration[2] != 0:
        print(
            f"Your number of seconds in day(s), hour(s), minute(s) and second(s): {duration[2]} day(s); {duration[3]} hour(s); {duration[4]} minute(s); {duration[5]} second(s)")
    elif duration[3] != 0:
        print(
            f"Your number of seconds in hour(s), minute(s) and second(s): {duration[3]} hour(s); {duration[4]} minute(s); {duration[5]} second(s)")
    elif duration[4] != 0:
        print(
            f"Your number of seconds in minute(s) and second(s): {duration[4]} minute(s); {duration[5]} second(s)")

    duration_sec = int(input("Please, enter a number larger to calculate the year,month, days, hours, minutes: "))

'''
2.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
a.	Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
b.	К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
c.	* Решить задачу под пунктом b, не создавая новый список.

'''

array_odd_of_numbers = []
sum_val = 0

for i in range(1, 1000, 2):
    i = i**3
    array_odd_of_numbers.append(i)

for val in array_odd_of_numbers:
    sum_num = 0
    while val > 0:
        sum_num += val % 10
        val = val // 10
        if sum_num % 7 == 0:
            sum_val += val
print(sum_val)


sum_val = 0

for i in array_odd_of_numbers:
    sum_num_17 = 0
    i += 17
    while i > 0:
        sum_num_17 += i % 10
        i = i // 10
        if sum_num_17 % 7 == 0:
            sum_val += i


print(sum_val)


# Еще одно решение:
array_odd_of_numbers = []
sum_val = 0
for i in range(1, 1000, 2):
    i = i**3 + 17
    sum_num = 0
    while i > 0:
        sum_num += i % 10
        i = i // 10
        if sum_num % 7 == 0:
            sum_val += i
print(sum_val)

'''
3.	Реализовать склонение слова «процент» для чисел до 20. 
Например, задаем число 5 — получаем «5 процентов», 
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''

percent = ['процент', 'процентов', 'процента']

i = int(input("Please, enter any number from 0 to ∞: "))

if (i % 100) > 10 and (i % 100) < 20:
    print(i, percent[1], end=' ')
elif i % 10 == 1:
    print(i, percent[0], end=' ')
elif (i % 10) > 1 and (i % 10) < 5:
    print(i, percent[2], end=' ')
else:
    print(i, percent[1], end=' ')