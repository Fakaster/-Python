from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {"Красный": 7, "Желтый": 2, "Зеленый": 5}
    __color_order = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for el in cycle(TrafficLight.__color_order):
            print(el)
            sleep(TrafficLight.__color[el])


my_class = TrafficLight()
my_class.running()
