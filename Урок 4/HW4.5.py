from functools import reduce


def calc(a, b):
    return a * b


first_list = [i for i in range(100, 1001) if i % 2 == 0]
print(f"{first_list}")
print(f"{reduce(calc, first_list)}")
