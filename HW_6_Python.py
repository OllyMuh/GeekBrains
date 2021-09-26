from time import sleep

"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
 реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
 Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
 на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
 зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу можно усложнить, реализовав
 проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""


class TrafficLight:
    __color = ("Красный", "Желтый", "Зеленый")

    def running(self):
        i = 0
        while i < 3:
            print(f'Цвет светофора {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)
            i += 1


first = TrafficLight()
first.running()

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
 для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def count_asf(self):
        thickness_sm = float(input("Какая толщина полотна в см?: "))
        mass_per_1m_1sm = 25
        return f"Потребуется {round(self.__width * self.__length * thickness_sm * mass_per_1m_1sm/1000)} тонн"


my_road = Road(5000, 20)
print(my_road.count_asf())

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. 

Создать класс Position (должность) на базе класса Worker. В классе Position 
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения 
атрибутов, вызвать методы экземпляров).
"""


class Worker:

    dict_income = {
        "wage": 1000,
        "bonus": 200,
    }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = Worker.dict_income.get("wage")
        self.total_income = self.__income + Worker.dict_income.get("bonus")

    def get_income(self):
        print(self.__income)


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f"Для должности {self.position} общий доход с учетом премии равен {self.total_income} рублей")


ivanov = Position("Иван", "Иванов", "бухгалтер")

ivanov.get_full_name()
ivanov.get_income()
ivanov.get_total_income()

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
. А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    max_speed = 200
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        print(f"Создан экземпляр автомобиля {self.name} цвет {self.color}")

    def go(self):
        Car.speed = int(input("Введите скорость, с которой eдет автомобиль: "))
        if Car.speed > Car.max_speed:
            print("Ваш автомобиль не может так разогнаться")
        else:
            print(f"Автомобиль {self.name} цвет {self.color} поехал со скоростью {self.speed} км/ч")

    def stop(self):
        Car.speed = 0
        print(f"Автомобиль {self.name} цвет {self.color} остановился, его скорость {self.speed} км/ч")

    def car_turn(self):
        direction = int(input("Введите направление поворота 1 - для поворота направо, 2 - для поворота налево: "))
        if direction == 1:
            print(f"Автомобиль {self.name} цвет {self.color} повернул направо")
        elif direction == 2:
            print(f"Автомобиль {self.name} цвет {self.color} повернул налево")
        else:
            print("Вы ввели некорректное значение для поворота - учите цифры)))")

    def show_speed(self):
        if Car.speed == 0:
            print(f"Автомобиль {self.name} цвет {self.color} стоит")
        elif Car.speed >= Car.max_speed:
            print(f"Вы едете с максимальной скоростью {self.max_speed} км/ч, потому что больше не получается")
        else:
            print(f"Автомобиль {self.name} цвет {self.color} едет со скоростью {self.speed} км/ч")

    def is_police_car(self):
        if Car.is_police:
            print("Это машина полиции")
        else:
            print("Это не полицейская машина")

my_car = Car("синий", "пуля")
my_car.go()
my_car.stop()
my_car.car_turn()
my_car.show_speed()
my_car.is_police_car()


class TownCar(Car):

    def show_speed(self):
        if Car.speed == 0:
            print(f"Городской автомобиль {self.name} цвет {self.color} стоит")
        elif self.speed > 60:
            print(f"Вы едете со скоростью {self.speed} км/ч и превышаете установленную для города скорость 60 км/ч"
                  f" на {self.speed - 60} км/ч!")
        else:
            print(f"Городской автомобиль {self.name} цвет {self.color} едет со скоростью {self.speed} км/ч")


class WorkCar(Car):
    Car.max_speed = 80

    def show_speed(self):
        if Car.speed == 0:
            print(f"Рабочий автомобиль {self.name} цвет {self.color} стоит")
        elif self.speed > 40:
            print(f"Вы едете со скоростью {self.speed} км/ч и превышаете установленную для {self.name} скорость 40 км/ч!")
        else:
            print(f"Рабочий автомобиль {self.name} цвет {self.color} едет со скоростью {self.speed} км/ч")


class SportCar(Car):
    Car.max_speed = 300


class PoliceCar(SportCar):
    Car.is_police = True


my_towncar = TownCar("красный", "городская")
my_towncar.go()
my_towncar.show_speed()

my_workcar = WorkCar("зеленый", "рабочая")
my_workcar.go()
my_workcar.show_speed()

my_sportcar = SportCar("желтый", "спортивная")
my_sportcar.go()
my_sportcar.show_speed()

my_policecar = PoliceCar("правильный", "полицейская")
my_policecar.is_police_car()

"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw 
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), 
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен 
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого 
экземпляра.
"""


# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print(f"Запуск отрисовки {self.title}")
#
#
# class Pen(Stationery):
#     def draw(self):
#         print(f"Я пишу текст - я {self.title}")
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f"Я рисую тонкую линию, которую можно стереть ластиком, я - {self.title}")
#
#
# class Handle(Stationery):
#     def draw(self):
#         print(f"Я могу рисовать толстыми яркими линиями, я - {self.title}")
#
#
# my_stationery = Stationery("канцелярская принадлежность")
# my_pen = Pen("ручка")
# my_pencil = Pencil("карандаш")
# my_handle = Handle("маркер")

# my_stationery.draw()
# my_pen.draw()
# my_pencil.draw()
# my_handle.draw()
