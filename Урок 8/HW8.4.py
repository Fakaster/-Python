class Equipment:

    def __init__(self, name, body_material, body_color):
        self.name = name
        self.body_material = body_material
        self.body_color = body_color

    def turn_on(self):
        print(f"Объект {self.name} включился")

    def turn_off(self):
        print(f"Объект {self.name} выключился")

    def __str__(self):
        return self.name


class Warehouse:
    def __init__(self, name: str):
        self.assortment = []

    def add_assortment(self, name_equipment: Equipment):
        self.assortment.append(name_equipment)

    def show_assortment(self):
        print("Техника хранящаяся на складе ", *self.assortment)

    @property
    def get_assortment(self):
        return self.assortment


class Printer(Equipment):
    def __init__(self, name, body_material, body_color, print_color, paint_type, print_volume):
        Equipment.__init__(self, name, body_material, body_color)
        self.print_color = print_color
        self.paint_type = paint_type
        self.print_volume = print_volume

    @staticmethod
    def my_print(text):
        print(f'Текст "{text}" отправлен на печать')


class Scanner(Equipment):
    def __init__(self, name, body_material, body_color, scanning_speed, multi_scanning):
        Equipment.__init__(self, name, body_material, body_color)
        self.scanning_speed = scanning_speed
        self.multi_scanning = multi_scanning

    @staticmethod
    def my_scan(text):
        print(f'Текст "{text}" отсканирован')


class Xerox(Equipment):
    def __init__(self, name, body_material, body_color, print_color, paint_type, print_volume,
                 scanning_speed, multi_scanning):
        Equipment.__init__(self, name, body_material, body_color)
        self.print_color = print_color
        self.paint_type = paint_type
        self.print_volume = print_volume
        self.scanning_speed = scanning_speed
        self.multi_scanning = multi_scanning

    @staticmethod
    def my_print(text):
        print(f'Текст "{text}" отправлен на печать')

    @staticmethod
    def my_scan(text):
        print(f'Текст "{text}" отсканирован')

    @staticmethod
    def my_photocopy(text):
        print(f'Сделана ксерокопия текста - {text}')


printer = Printer('принтер', 'plastic', "black", 'black', 'toner', 500)
scanner = Scanner('сканер', 'plastic', "black", 20, True)
xerox = Xerox('ксерокс', 'metal', "silver", 'colored', 'toner', 310, 20, True)
warehouse = Warehouse('Склад орг. техники')
printer.my_print('Что - то')
scanner.my_scan('Что - то')
xerox.my_print('Что - то')
xerox.my_scan('Что - то')
xerox.my_photocopy('Что - то')
warehouse.add_assortment(printer)
warehouse.add_assortment(scanner)
warehouse.add_assortment(xerox)
warehouse.show_assortment()
[i.turn_on() for i in warehouse.get_assortment]
[i.turn_off() for i in warehouse.get_assortment]



