# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
import time

class TrafficLight:

    colors = ['red', 'yellow', 'green']
    sleep_time = [7, 2, 5]
    __color = 'red'

    def running(self, color):
        current_index = TrafficLight.colors.index(self.__color)
        color = color.lower()
        new_index = TrafficLight.colors.index(color)

        if new_index != (current_index + 1) % len(TrafficLight.colors):
            raise ValueError(f'Unexpected color [color={TrafficLight.colors[new_index]}]')
        self.__color = color
        print(f"Switching to {color}")
        time.sleep(TrafficLight.sleep_time[new_index])


traffic_light1 = TrafficLight()
traffic_light2 = TrafficLight()
traffic_light1.running('Yellow')
traffic_light1.running('green')
traffic_light1.running('red')
traffic_light1.running('Yellow')
traffic_light1.running('green')
traffic_light2.running('Yellow')