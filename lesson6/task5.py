# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Пишем ручкой {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Рисуем карандашом {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Чертим маркером {self.title}')


paintbrush = Stationery('привет')
paintbrush.draw()
pen = Pen('текст')
pen.draw()
pencil = Pencil('картину')
pencil.draw()
handle = Handle('эскиз')
handle.draw()
