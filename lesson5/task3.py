# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
# with open('file_3.txt', encoding='utf-8') as f_3:
#     for line in f_3:
#         lst = line.split()
#         if int(lst[1]) < 20000:
#             print(lst[1])
#         print(sum(int(lst[1]))/len(lst[1]))

with open('file_3.txt', 'r', encoding='utf-8') as my_file:
    sal = []
    poor = []
    for line in my_file:
        if len(line) < 2:
            continue
        arr = line.strip('\n').split(' ')
        salary = int(arr[1])
        if salary < 20000:
            poor.append(arr[0])
        sal.append(salary)
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(sal) / len(sal)}')
