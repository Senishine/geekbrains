# 5.Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
while True:
    n = int(input('Введите положительное число или 0, если хотите выйти: '))
    if n < 0:
        continue
    elif n == 0:
        break
    index = len(my_list)
    for i in range(len(my_list)):
        if n > my_list[i]:
            index = i
            break
    my_list.insert(index, float(n))

    print(f'{my_list}')
