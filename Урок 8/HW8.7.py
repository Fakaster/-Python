class Complex_number:
    def __init__(self, re_z: int, im_z: int):
        self.lst = {}
        try:
            self.lst['re_z'] = int(re_z)
        except ValueError:
            print("Вы ввели не действительную часть комплексного числа")
        if isinstance(im_z, int):
            self.lst['im_z'] = im_z
        else:
            try:
                self.lst["im_z"] = int(im_z[:-1])
            except TypeError:
                print('Вы ввели не мнимую часть комплексного числа')

    def __str__(self):
        return str(self.lst['re_z']) + ('+' if self.lst["im_z"] >= 0 else "") + str(self.lst["im_z"]) + 'i'

    def __add__(self, other):
        lst = {'re_z': 0, "im_z": 0}
        lst['re_z'] = self.lst['re_z'] + other.lst['re_z']
        lst['im_z'] = self.lst["im_z"] + other.lst["im_z"]
        return lst

    def __mul__(self, other):
        lst = {'re_z': 0, "im_z": 0}
        lst['re_z'] = self.lst['re_z'] * other.lst['re_z'] + self.lst["im_z"] * other.lst["im_z"] * -1
        lst['im_z'] = self.lst['re_z'] * other.lst["im_z"] + self.lst["im_z"] * other.lst['re_z']
        return lst


a = Complex_number(1, 5)
b = Complex_number(2, 3)
print(a)
print(b)
print(a + b)
print(a)
print(a * b)
# print(a.lst)
