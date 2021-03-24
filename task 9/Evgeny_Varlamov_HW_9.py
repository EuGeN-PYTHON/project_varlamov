import time

"""
1.	Создать класс TrafficLight (светофор):
"""
class ColorError(Exception):
   pass

class TrafficLight:
    _color = 'red'

    def running(self):
        if TrafficLight._color != 'red':
            raise ColorError("the attribute must have a color - red")
            quit()
        time.sleep(7)
        print(TrafficLight._color)
        TrafficLight._color = 'yellow'
        time.sleep(2)
        print(TrafficLight._color)
        TrafficLight._color = 'green'
        time.sleep(5)
        print(TrafficLight._color)

a = TrafficLight()
a.running()
print(a._color)
# a.running()


"""
2.	Реализовать класс Road (дорога).

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, thickness):
        mass = self._length * self._width * 25 * thickness
        return f" {mass} kg. or {mass//1000} t. and {mass%1000} kg."

rublevka = Road(20,5000)
print(rublevka.get_mass(5))

"""
3.	Реализовать базовый класс Worker (работник):
●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""

class Worker:
    def __init__(self, name, surname, wage, bonus, position = None,):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)
        pass

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]} rub.'

a = Position('Ivan', 'Ivanov', 5000, 500)
print(a.get_full_name())

print(a.get_total_income())

"""
4.	Реализуйте базовый класс Car:
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

"""

class Car:
    def __init__(self, speed, color, name, is_police = None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print("The car is going")

    def stop_car(self):
        print("The car is stop")

    def turn(self, direction):
        print(f"The car turned {direction}")

    def show_speed(self):
        print(f"Speed is {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass

    def show_speed(self):
        if self.speed > 60:
            print(f"I stopped you for speeding!!! Speed is {self.speed}")
        else:
            print(f"Speed is {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass

    def show_speed(self):
        if self.speed > 40:
            print(f"I stopped you for speeding!!! Speed is {self.speed}")
        else:
            print(f"Speed is {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass

vw = Car(60,'silver', 'VW')
vw.show_speed()

town_car = TownCar(61, 'black', 'BMW')
town_car.show_speed()

work_car = WorkCar(41, 'white', 'Volvo')
work_car.show_speed()

"""
5.	Реализовать класс Stationery (канцелярская принадлежность):
●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки Pen")

class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки Pencil")

class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки Handle")

a = Stationery("Brush")
a.draw()

b = Pen('Pen')
b.draw()

c = Pencil('Pencil')
c.draw()

d = Handle('Handle')
d.draw()