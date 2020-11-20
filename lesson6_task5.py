# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} running..")


class Pen(Stationery):
    def draw(self):
        print(f"custom {self.title} drawing")


class Pencil(Stationery):
    def draw(self):
        print(f"custom {self.title} drawing")


class Marker(Stationery):
    def draw(self):
        print(f"custom {self.title} drawing")


items = [Pen("pen"), Pencil("pencil"), Marker("marker")]
for item in items:
    item.draw()
