# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()для реализации операции сложения двух объектов класса Matrix(двух матриц)
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        if len(set(map(len, matrix))) != 1:
            raise ValueError('Некорректная матрица')
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join(str(v) for v in i) for i in self.matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Матрицы разных рамеров')
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return self


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(m))
b = Matrix([[3, 4, 6], [5, 9, 8], [1, 7, 2]])
print(b)
print(m + b + b)
