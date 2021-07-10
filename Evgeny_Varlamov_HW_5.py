"""
1. Генератор через yield
"""

def get_odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


odd_nums = get_odd_nums(int(input('Please, input any number: ')))
#
# print(next(odd_nums))
# print(next(odd_nums))
# print(next(odd_nums))
# print(next(odd_nums))
# print(next(odd_nums))
print(type(odd_nums), *odd_nums)


"""
2* Генератор без yield
"""

n = int(input('Please, input any number: '))
odd_nums = (i for i in range(1, n + 1,2))

# print(next(odd_nums))
# print(next(odd_nums))
# print(next(odd_nums))
# print(next(odd_nums))
# print(next(odd_nums))
print(type(odd_nums), *odd_nums)

"""
3. вернуть при помощи генератора кортежи вида (<tutor>, <klass>)
"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '10A'
]

def get_gen_student():
    for i in range(len(tutors)):
        if i >= len(klasses):
            yield (tutors[i], None)
        else:
            yield (tutors[i], klasses[i])

gen_student = get_gen_student()

print(type(gen_student))
print(*gen_student)

"""
4. Необходимо вывести те его элементы, значения которых больше предыдущего
result = [12, 44, 4, 10, 78, 123]
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[i] for i in range(1, len(src)-1) if src[i-1] < src[i]]
print(result)

"""
5. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
result = [23, 1, 3, 10, 4, 11]
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [i for i in src if src.count(i) == 1]
print(result)