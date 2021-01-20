# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,color,name,is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля превышена и равна {self.speed}')
        else:
            print(f'Текущая скорость автомобиля - {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Будьте внимательны! Скорость автомобиля превышена и равна {self.speed}')
        else:
            print(f'Текущая скорость автомобиля - {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name, is_police)


ferrari = Car(350, 'red', 'ferrari')
ferrari.go()
ferrari.stop()
ferrari.turn('направо')
ferrari.show_speed()
volvo = TownCar(200, 'brown', 'volvo', False)
volvo.go()
volvo.stop()
volvo.turn('налево')
volvo.show_speed()
jaguar = SportCar(350, 'gray', 'jaguar')
jaguar.show_speed()
kamaz = WorkCar(90, 'orange', 'kamaz')
kamaz.show_speed()
police_car = PoliceCar(120, 'white', 'Ford', True)
police_car.go()
police_car.stop()
police_car.turn('направо')
police_car.show_speed()
