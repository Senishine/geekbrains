# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Storage:
    def __init__(self):
        self._dict = {}
        pass


class Department(Storage):
    def __init__(self, name):
        Storage.__init__(self)
        self.name = name
        pass


class OfficeEquipment:
    def __init__(self, name, price, make, model):
        self.name = name
        self.price = price
        self.make = make
        self.model = model


class Xerox(OfficeEquipment):
    def __init__(self, price, make, model):
        super().__init__('Xerox', price, make, model)


class Printer(OfficeEquipment):
    def __init__(self, price, make, model):
        super().__init__('Printer', price, make, model)


class Scanner(OfficeEquipment):
    def __init__(self, price, make, model):
        super().__init__('Scanner', price, make, model)


printer_1 = Printer(10000, 'Hewlett-Packard', 'CX-500')
print(Scanner(2000, 'Samsung', 'S500'))
scanner_1 = Scanner(2000, 'Samsung', 'S500')
print(scanner_1)
xerox_1 = Xerox(5000, 'Lenovo', 'CopyLeft')
