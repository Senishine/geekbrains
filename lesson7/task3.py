# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого
# числа.

class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return f'Cell: {self.number}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        cell_decrease = self.number - other.number
        if cell_decrease > 0:
            return Cell(round(self.number - other.number))
        raise ValueError('Невозможно вычесть большую клетку из меньшей')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, num_of_cells):
        result = ''
        if num_of_cells <= 0:
            raise ValueError(f'Некорректное значение ячеек [{num_of_cells}]')
        result += ('*' * num_of_cells + '\n') * (self.number // num_of_cells)
        result += '*' * (self.number % num_of_cells) + '\n'
        return result


cell_1 = Cell(20)
cell_2 = Cell(28)
cell_3 = Cell(30)
res = None
try:
    res = cell_2 + cell_1 - cell_3 - cell_3 - cell_2
except ValueError as err:
    print(f"Ой ошибка сообщение: {err}")
    res = Cell(123)

print(res)
print(cell_2 + cell_1)
print(cell_2 - cell_1)
print(cell_2 * cell_1)
print(cell_2 / cell_1)
print(cell_1.make_order(6))
