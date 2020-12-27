# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

goods_count = int(input('Введите кол-во товаров: '))
name_key = 'название'
price_key = 'цена'
count_key = 'количество'
measurement_key = 'единица измерения'

goods = []
for i in range(1, goods_count + 1):
    name = input('Введите название товара: ')
    price = float(input('Введите цену товара: '))
    count = int(input('Введите количество товара: '))
    measurement = input('Введите единицу измерения товара: ')
    goods.append((i, {
        name_key: name,
        price_key: price,
        count_key: count,
        measurement_key: measurement
    }))
print(f'{goods}')

analytics = {
    name_key: [],
    price_key: [],
    count_key: [],
    measurement_key: []
}
for i in goods:
    dict_ex = i[1]
    analytics[name_key].append(dict_ex[name_key])
    analytics[price_key].append(dict_ex[price_key])
    analytics[count_key].append(dict_ex[count_key])
    analytics[measurement_key].append(dict_ex[measurement_key])
print(f'{analytics}')
