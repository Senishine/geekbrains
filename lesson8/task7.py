# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNums:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNums(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNums(self.a * other.a, self.b * other.b)

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNums(11, -1)
z_2 = ComplexNums(4, 10)
print(z_1)
print(z_1 + z_2 + z_1)
print(z_1 * z_2)
