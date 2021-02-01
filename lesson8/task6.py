# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

import numbers


def check_valid_str(s: str):
    if s is None or len(s) == 0:
        raise ValueError('Invalid string')
    return s


def check_price(price):
    if not isinstance(price, numbers.Number) or float(price) <= 0:
        raise ValueError('Invalid price')
    return price


def check_count(count) -> int:
    if not isinstance(count, numbers.Number) or int(count) <= 0:
        raise ValueError(f'Invalid count [value={count}]')
    return count


class OfficeEquipment:
    def __init__(self, name: str, price: float, make: str, model: str):
        self.name = check_valid_str(name)
        self.price = check_price(price)
        self.make = check_valid_str(make)
        self.model = check_valid_str(model)

    def __repr__(self):
        return f'{self.name}[price={self.price}, make={self.make}, model={self.model}]'

    def unique_name(self):
        return f'{self.name}:{self.make}:{self.model}'


class Item:
    def __init__(self, office_eq: OfficeEquipment, count: int):
        self.office_eq = office_eq
        self.count = check_count(count)

    def __repr__(self):
        return f'[count={self.count}, name={self.office_eq.name}, price={self.office_eq.price}, ' \
               f'make={self.office_eq.make}, model={self.office_eq.model}]'


class Storage:
    def __init__(self):
        self._dict = {}
        pass

    def accept(self, item: Item):
        prev: Item = self._dict.get(item.office_eq.unique_name())
        if prev is None:
            self._dict[item.office_eq.unique_name()] = item
        else:
            self._dict[item.office_eq.unique_name()] = Item(item.office_eq, prev.count + item.count)

    def move_to(self, req_item: Item, storage):
        check_count(req_item.count)
        rem_item = self._dict.get(req_item.office_eq.unique_name())
        if rem_item is None:
            raise ValueError(f'No such item in storage [requested item={req_item}]')
        if rem_item.count < req_item.count:
            raise ValueError(f'Requested items count more than remainder in storage '
                             f'[requested={req_item.count}, remainder={rem_item.count}]')
        storage.accept(req_item)
        self._dict[rem_item.office_eq.unique_name()] = Item(rem_item.office_eq, rem_item.count - req_item.count)

    def print_all(self):
        print(f'Items in storage: {self._dict}')


class Department(Storage):
    def __init__(self, name: str):
        Storage.__init__(self)
        self.name = check_valid_str(name)
        pass

    def print_all(self):
        print(f'Items in storage: [department={self.name}, items={self._dict}]')


class Xerox(OfficeEquipment):
    def __init__(self, price, make, model):
        super().__init__('Xerox', price, make, model)


class Printer(OfficeEquipment):
    def __init__(self, price, make, model):
        super().__init__('Printer', price, make, model)


class Scanner(OfficeEquipment):
    def __init__(self, price, make, model):
        super().__init__('Scanner', price, make, model)


main_storage = Storage()
dep1 = Department('IT')
dep2 = Department('Sales')

printer_1 = Printer(22000, 'Hewlett-Packard', 'CX-500')
scanner_1 = Scanner(17000, 'Samsung', 'S500')
xerox_1 = Xerox(25000, 'Lenovo', 'CopyLeft')
printer_2 = Printer(22000, 'Hewlett-Packard', 'X-200')
scanner_2 = Scanner(17000, 'Canon', 'PIXMA')
xerox_2 = Xerox(25000, 'Pantum', 'M6607')

main_storage.accept(Item(printer_1, 3))
main_storage.accept(Item(printer_1, 5))
main_storage.accept(Item(scanner_2, 5))
main_storage.accept(Item(scanner_1, 6))
main_storage.accept(Item(printer_2, 6))
main_storage.accept(Item(xerox_1, 4))
main_storage.accept(Item(xerox_2, 3))

main_storage.move_to(Item(scanner_1, 1), dep1)
main_storage.move_to(Item(printer_1, 2), dep1)
main_storage.move_to(Item(scanner_1, 1), dep1)
main_storage.move_to(Item(xerox_1, 2), dep2)

main_storage.print_all()
dep1.print_all()
dep2.print_all()
