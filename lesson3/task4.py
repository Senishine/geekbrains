# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    return x**y


def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res


value_1 = int(input('Введите первое число: '))
value_2 = int(input('Введите второе число: '))
print(my_func(value_1, value_2))
print(my_func2(value_1, value_2))
