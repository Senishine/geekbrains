# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('my_hometask_file.txt', 'w')
while True:
    data = input('Введите данные или Enter, если закончили: ')
    if data == '':
        break
    f.write(data + '\n')
f.close()


