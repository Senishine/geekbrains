# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('file_2.txt', 'r', encoding='utf-8') as f_2:
    line_count = 0
    for line in f_2:
        line_count += 1
        result = list(filter(str.isalpha, line.split()))
        print(f'Количестве слов в встроке - {len(result)}, строка № {line_count}')
print(f'Количестве строк - {line_count}')
