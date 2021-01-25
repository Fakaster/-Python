from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def put_on(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def show_options(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, name, size):
        self.size = size
        self.name = name

    def put_on(self):
        print(f'Вы надели {self.name}')

    def remove(self):
        print(f"Вы сняли {self.name}")

    @property
    def show_options(self):
        print(self.__dict__)


class Coat(Clothes):
    pass


class Costume(Clothes):
    def __init__(self, name, growth):
        self.growth = growth
        self.name = name


a = Coat('Пальто', 25)
b = Costume("Костюм", 250)
b.remove()
a.put_on()
a.show_options
b.show_options

print(f'Общее требуемое кол-во ткани - {a.size / 6.5 + 0.5 + 2 * b.growth:.2f}')
