# 7. Создать вручную и заполнить несколькими строками текстовый файл,в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

lst = []
firms_profit = {}
avg_dict = {}
total_profit = 0
firm_prof_counter = 0
with open('file_7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        firm, _, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms_profit[firm] = profit
        if profit >= 0:
            total_profit += profit
            firm_prof_counter += 1
    try:
        average_profit = total_profit / firm_prof_counter
    except ZeroDivisionError:
        print('Нет фирм с выручкой')

    avg_dict['avg_profit'] = average_profit
    lst = [firms_profit, avg_dict]

with open('file_7.json', 'w', encoding='utf-8') as js_file:
    json.dump(lst, js_file, ensure_ascii=False)

js_f = json.dumps(lst, ensure_ascii=False)
print(f'Создан файл с расширением json {js_f}')


