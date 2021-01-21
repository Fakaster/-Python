class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income, 'bonus': income * 0.4}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


a = Position('Серж', "Абрамов", "рядовой", 15000)
a.get_full_name()
a.get_total_income()
