# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyException(ZeroDivisionError):
    def __init__(self, msg, divident, divisor):
        ZeroDivisionError.__init__(self, msg)
        self.divident = divident
        self.divisor = divisor


x = int(input('Введите число - делимое: '))
y = int(input('Введите число - делитель: '))

try:
    if y == 0:
        raise MyException('Вы ввели 0, на ноль делить нельзя', x, y)
except MyException as err:
    print(f'Ошибка деления, делимое: {err.divident}, делитель: {err.divisor}')
else:
    print(f'Частное равно {x / y:.2f}')
