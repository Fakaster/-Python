class Road:
    def __init__(self, length, width):
        self.___length = length
        self.___width = width

    def get_weight(self, mass_for_m, thickness):
        self.mass_for_m = mass_for_m
        self.thickness = thickness
        return self.___length * self.___width * self.mass_for_m * self.thickness


a = Road(20, 5000)
print(a.get_weight(25, 5))

