class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула на {self.direction}')

    def show_speed(self):
        print(f'Ваша скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили допустимую скорость {60} км/ч, сбросьте {self.speed - 60} км/ч')
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили допустимую скорость {40} км/ч, сбросьте {self.speed - 40} км/ч')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


def get_my_info(obj):
    print(f'Вы находитесь за рулем {obj.name}, цвет машины - {obj.color}')
    obj.go()
    obj.show_speed()
    obj.turn('лево')
    obj.stop()



audi = PoliceCar(220, 'blue', 'Audi Q8', True)
get_my_info(audi)
volvo = TownCar(75, 'black', "Volvo S80", False)
get_my_info(volvo)
lada = WorkCar(45, 'white', 'Lada Largus', False)
get_my_info(lada)
porsche = SportCar(180, 'black', 'Porsche Panamera', False)
get_my_info(porsche)
