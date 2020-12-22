a = 1
b = 3
c = a + b
d = a // b
drink = 'coca-cola'
print(c, d)
print('I like to drink ' + drink)

number = int(input("Введите целое число: "))
fl_number = float(input('Введите число с дробной частью: '))
name = input('Введите ваше имя: ')
city = input('Введите ваш город: ')


print('Добрый день, {}, Вы из города {}'.format(name, city))
print('Целое число - {}, вещественное число - {:.2f}'.format(number, fl_number))
