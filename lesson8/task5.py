# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

class Item:
    def __init__(self, office_eq, count):
        self.office_eq = office_eq
        self.count = count

    def __repr__(self):
        return f'[count={self.count}, name={self.office_eq.name}, price={self.office_eq.price}, ' \
               f'make={self.office_eq.make}, model={self.office_eq.model}]'

class Storage:
    def __init__(self):
        self._dict = {}
        pass

    def accept(self, office_eq, count):
        self._dict[office_eq.unique_name()] = Item(office_eq, count)

    def move_to(self, item, storage):
        item = self._dict[item.office_eq.unique_name()]
        storage.accept(item.office_eq, item.count)
        self._dict[item.office_eq.name] = Item(item.office_eq, item.count - item.count)

    def print_all(self):
        print(f'Items in storage: {self._dict}')


class Department(Storage):
    def __init__(self, name):
        Storage.__init__(self)
        self.name = name
        pass

    def print_all(self):
        print(f'Items in storage: [department={self.name}, items={self._dict}]')


class OfficeEquipment:
    def __init__(self, name, price, make, model):
        self.name = name
        self.price = price
        self.make = make
        self.model = model

    def __repr__(self):
        return f'{self.name}[price={self.price}, make={self.make}, model={self.model}]'

    def unique_name(self):
        return f'{self.name}:{self.make}:{self.model}'


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

printer_1 = Printer(10000, 'Hewlett-Packard', 'CX-500')
scanner_1 = Scanner(2000, 'Samsung', 'S500')
xerox_1 = Xerox(5000, 'Lenovo', 'CopyLeft')

main_storage.accept(printer_1, 4)
main_storage.accept(scanner_1, 3)
main_storage.accept(xerox_1, 7)

dep1 = Department('IT')
dep2 = Department('Sales')

main_storage.move_to(Item(printer_1, 3), dep1)
main_storage.move_to(Item(scanner_1, 1), dep1)
main_storage.move_to(Item(xerox_1, 2), dep1)
main_storage.move_to(Item(xerox_1, 5), dep2)

dep1.print_all()
dep2.print_all()
