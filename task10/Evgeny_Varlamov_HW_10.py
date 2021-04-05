from abc import ABC, abstractmethod


"""
1. Реализовать класс MATRIX
"""

class Matrix:

    def __init__(self, args):
        self.list = args
        self.num_str = len(args)
        self.num_columns = len(args[0])

    def __str__(self):
        str_list = ""
        for str in self.list:
            new_str = ""
            for i in str:
                new_str += f"{i}  "
            str_list += f'{new_str}\n'
        return str_list

    def __add__(self, other):
        c = []
        try:
            for str in range(len(self.list)):
                d = []
                for i in range(len(self.list[str])):
                    d.append(self.list[str][i] + other.list[str][i])
                c.append(d)
            return Matrix(c)
        except IndexError:
            return ("Сложение невозможно: Матрицы разных размеров")


a = Matrix([[31, 22, 1],[37, 43, 1],[51, 86, 1]])
b = Matrix([[3,5, 1],[2,4,1],[-1,64,1]])
c = Matrix([[3,5,8,3],[8,3,7,1]])

e = a + b
print(e)

f = b+c
print(f)

"""
2.	 
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

class Dress(ABC):

    @abstractmethod
    def get_consumption(self):
        pass




class Coat(Dress):

    def __init__(self, v):
        self.v = v

    @property
    def get_consumption(self):
        cons = self.v / 6.5 + 0.5
        return cons


class Costume(Dress):

    def __init__(self, h):
        self.h = h

    @property
    def get_consumption(self):
        cons = 2 * self.h + 0.3
        return cons

red_coat = Coat(5)
blue_costume = Costume(50)

print(red_coat.get_consumption)
print(blue_costume.get_consumption)

"""
3.	Осуществить программу работы с органическими клетками, состоящими из ячеек. 
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.

"""

class Cell:

    def __init__(self, num):
        self.num = num

    def __add__(self,other):
        sum = self.num + other.num
        return Cell(sum)

    def __sub__(self, other):
        if self.num < other.num:
            return print("Количество ячеек уменьшаемой клетки, меньше вычитаемой")
        result = self.num - other.num
        return Cell(result)

    def __mul__(self,other):
        result = self.num * other.num
        return Cell(result)

    def __floordiv__(self, other):
        result = self.num // other.num
        return Cell(result)

    def __str__(self):
        return f"{self.num}"

    def make_order(self,num_str):
        str = ""
        counter = self.num
        while counter > 0:
            for i in range(num_str):
                str += "*"
                counter -= 1
                if counter == 0:
                    return str
            str += "\n"


cell_1 = Cell(41)
cell_2 = Cell(12)

print(cell_1.make_order(5))
