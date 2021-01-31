# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def int_date(cls, date):
        date_list = []
        for i in date.split('-'):
            date_list.append(i)
        return [int(elem) for elem in date_list]

    @staticmethod
    def check_date(date):
        date = list(map(int, date.split('-')))
        if 1 < date[0] < 31:
            if  1 < date[1] < 13:
                if 1900 < date[2] < 2021:
                    return f'Дата введена верно'
                else: f'Год должен быть в диапазоне 1900 - 2021'
            else: f'Месяц должен быть в диапазоне от 1 - 12'
        else: f'День должен быть в диапазоне от 1 - 31'


date_1 = Date('15-2-2020')
print(date_1.check_date('20-03-2020'))
print(date_1.int_date('15-2-2020'))
print(Date.check_date('30-09-2000'))
print(Date.int_date('11-11-2011'))