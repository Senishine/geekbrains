# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('Name called from decorator')
        return self.__name


    @abstractmethod
    def textile_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        Clothes.__init__(self, 'coat')
        self.size = size

    def textile_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        Clothes.__init__(self, 'suit')
        self.height = h

    def textile_consumption(self):
        return self.height * 2 + 0.3


def total_textile(arr):
    return sum(map(lambda item: item.textile_consumption(), arr))


clothes_items = []
my_coat = Coat(44)
print(my_coat.textile_consumption())
print(my_coat.name)
my_suit = Suit(44)
print(my_suit.textile_consumption())
clothes_items.append(my_coat)
clothes_items.append(my_suit)
print(total_textile(clothes_items))
