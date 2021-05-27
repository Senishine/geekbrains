# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import calendar


class Date:
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def int_date(cls, date):
        cls.check_date(date)
        date_list = []
        for i in date.split('-'):
            date_list.append(i)
        return [int(elem) for elem in date_list]

    @staticmethod
    def check_date(date):
        date = list(map(int, date.split('-')))

        if len(date) != 3:
            raise ValueError('Invalid date format')

        year = date[2]
        month = date[1]
        day = date[0]

        if year < 0:
            raise ValueError(f'Invalid year [year={year}]')

        if month > 12 or month < 1:
            raise ValueError(f'Invalid month [month={month}]')

        if day < 1:
            raise ValueError(f'Invalid day [day={day}]')

        if month == 2:
            if day > (29 if calendar.isleap(year) else 28):
                raise ValueError(f'Invalid days in feb [day={day}, leap year={calendar.isleap(year)}]')
            else:
                return

        if day > Date.days_per_month[month - 1]:
            raise ValueError(f'Invalid day [day={day}, expected days in month={Date.days_per_month[month - 1]}]')


date_1 = Date('15-2-2020')
date_1.check_date('20-03-2020')
print(date_1.int_date('15-2-2020'))
Date.check_date('30-09-2000')
print(Date.int_date('11-11-2011'))

Date.check_date('29-02-2020')
Date.check_date('29-02-2021')
