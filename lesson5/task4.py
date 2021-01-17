# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_data = []

with open('file_4.txt', 'r', encoding='utf-8') as f_4:
    for i in f_4:
        i = i.split(' ', 1)
        rus_data.append(rus[i[0]] + ' ' + i[1])
    print(rus_data)

with open('rus_file4.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.writelines(rus_data)