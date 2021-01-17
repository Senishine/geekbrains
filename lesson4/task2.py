# 2.Представлен список чисел. Необходимо вывести элементы исходного списка,значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

first_list = [int(random.random() * 100) for _ in range(1, 25)]
print(f"Исходный список - {first_list}")

print(f'Новый список - {[num for i, num in enumerate(first_list) if i > 0 and first_list[i] > first_list[i-1]]}')

