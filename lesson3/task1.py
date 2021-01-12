# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_with_error(a, b):
    if b == 0:
        raise ZeroDivisionError('Вы ввели 0, на ноль делить нельзя')
    else:
        return a / b


def divide(a, b):
    if b == 0:
        return float("inf")
    else:
        return a / b


x = float(input('Введите число - делимое: '))
y = float(input('Введите число - делитель: '))

try:
    print(f'Это функция с бесконечностью {divide(x, y)}')
    print(f'Это функция с ошибкой {divide_with_error(x, y)}')
except ZeroDivisionError as e:
    print('Ой что-то пошло не так ' + str(e))



