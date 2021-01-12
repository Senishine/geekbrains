# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def person_data(**data):
    return f"Имя: {data['name']}, Фамилия: {data['surname']}, Дата рождения: {data['birth']}, Город проживания: {data['town']}, " \
           f"эл почта: {data['email']}, телефон: {data['phone']}"


name = input('Input name: ')
last_name = input('Input your last name: ')
b_date = input('Input your birthday: ')
city = input('Input your city: ')
email = input('Input email: ')
tel = input('Input tel number: ')

print(person_data(name=name, surname=last_name, birth=b_date, town=city, email=email, phone=tel))
