"""
1.	Реализовать класс «Дата»
"""


class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def get_num_data(cls, data):
        day, month, year = data.split("-")
        return [int(day), int(month), int(year)]

    @staticmethod
    def get_my_data(data):
        day, month, year = data.split("-")
        if int(month) > 12 or int(month) < 1 or int(year) < 1 or int(year) > 10000:
            return "Введенная дата не валидна"
        else:
            return int(month), int(year)


print(Data.get_num_data("12-1-2001"))

print(Data.get_my_data("12-0-2001"))


"""
2.Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
"""


class Div0(Exception):
    def __init__(self, message="Enter another divisor"):
        super().__init__(message)


def div(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        raise Div0


print(div(1,1))

"""
3.	Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
"""


class Check_num:
    def __init__(self, text="data type is not number"):
        self.text = text

    @staticmethod
    def get_num():
        some_list = []
        data = ''
        while data != 'stop':
            data = input("Введите число, для выхода введите - stop:  ").lower()
            if data.isdigit() == True:
                some_list.append(int(data))
            elif data == "stop":
                return some_list
            elif data.isdigit() == False:
                print("data type is not number")


a = Check_num.get_num()
print(a)

"""
4.5.6. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.

"""


class StockEquipment:
    """
    класс описывающий склад оргтехники
    """
    def __init__(self):
        pass





class FrontOffice:
    pass

class BackOffice:
    pass



class Equipment:

    def __init__(self, weight, coast):
        self.weight = weight
        self.coast = coast


class Printer(Equipment):
    id_print = 0

    def __init__(self, weight, coast):
        super().__init__(weight, coast)
        self.id_print += 1


class Scaner(Equipment):
    id_scan = 0


    def __init__(self, weight, coast,):
        super().__init__(weight, coast)
        self.id_scan +=1


class Xerox(Equipment):
    id_xer = 0

    def __init__(self, weight, coast,):
        super().__init__(weight, coast, )
        self.id_xer +=1


a = Printer(1, 2)
# print(a.weight)


"""
7.	Реализовать проект «Операции с комплексными числами». 
"""


class ComplexNum:

    def __init__(self, num):
        self.num = num
        self.a = self.num[:self.num.index("+")].replace(" ", "").replace('+', '')
        self.b = self.num[self.num.index("+"):].replace(" ", "").replace("i", "")


    def __add__(self, other):
        return ComplexNum(f"{int(self.a) + int(other.a)} + {int(self.b) + int(other.b)}i")

    def __mul__(self, other):
        return ComplexNum(f"{int(self.a) * int(other.a) - int(self.b) * int(other.b)} "
                          f"+ {int(self.a) * int(other.b) + int(other.a) * int(self.b)}i")



com_num1 = ComplexNum("1+222i")
com_num2 = ComplexNum("22+3i")
com_num3 = com_num2 + com_num1
print(com_num3.num)
com_num4 = com_num2 * com_num1
print(com_num4.num)

