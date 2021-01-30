class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        __res_sub = self.quantity - other.quantity
        if __res_sub != 0:
            return __res_sub
        else:
            print("Возможно только при разном кол-ве клеток")

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return round(self.quantity / other.quantity)

    def make_order(self, qty_in_row):
        self.qty_in_row = qty_in_row
        __res = ""
        for i in range(1, self.quantity + 1):
            __res += "*"
            if i % self.qty_in_row == 0:
                __res += "\n"
        return __res


a = Cell(12)
b = Cell(6)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(5))
