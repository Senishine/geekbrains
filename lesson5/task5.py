# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('file_5.txt', 'w') as f_5:
    f_5.write(input('Введите целые числа через пробел: '))

with open('file_5.txt', 'r') as f_5:
    s = 0
    for val in f_5.read().split(' '):
        s += int(val)
    print(s)