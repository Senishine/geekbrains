# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    return int(a + b + c - (min(a, b, c)))


value_1 = int(input('Введите первое число: '))
value_2 = int(input('Введите второе число: '))
value_3 = int(input('Введите третье число: '))
print(f'Результат вычисления функции - {my_func(value_1, value_2, value_3)}')
