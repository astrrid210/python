# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car:
    max_speed = 150

    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = random.randint(10, self.max_speed)
        return f"{self.name} moving"

    def stop(self):
        self.speed = 0
        return f"{self.name}  stopped"

    def turn(self, direction):
        return f"{self.name}  turn {direction}"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        speed = super().show_speed()
        if speed > 60:
            print(f"speed limit for {__class__.__name__} alert: {speed}")
        return speed


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        speed = super().show_speed()
        if speed > 40:
            print(f"speed limit for {__class__.__name__} alert: {speed}")
        return speed


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


sport_car = SportCar("yellow", "sporty")
police_car = PoliceCar("blue", "ACAB")
work_car = WorkCar("black", "sturdy horse")
town_car = TownCar("white", "fluffy")

cars = [sport_car, police_car, work_car, town_car]
for car in cars:
    print(f"name: {car.name}, color: {car.color}, speed: {car.speed}, is_police: {car.is_police}")
for car in cars:
    print(car.go())
    print(car.turn("right"))
    print(car.turn("left"))
    print(f"{car.name} speed is ", car.show_speed())
    print(car.stop())
