earnings = float(input('Введите значение выручки: '))
cost = float(input('Введите значение издержек: '))

if earnings > cost:
    print('Фирма работает в плюс.')
    print(f'Рентабельность составляет {(1 - (cost / earnings)):.2f}')
    emp_count = int(input('Введите кол-во сотрудников в штате: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет {((earnings - cost) / emp_count):.2f}')
else:
    print('Фирма работает в минус.')


