class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


my_pen = Pen('Синяя ручка')
my_pen.draw()
my_pencil = Pencil('Мягкий карандаш')
my_pencil.draw()
My_handle = Handle('Черный маркер')
My_handle.draw()