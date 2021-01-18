from random import randrange


def get_factorial(num):
    for i in range(1, num + 1):
        yield i


num = randrange(5, 15)
print(f'Число до которого будем выводить символы - {num}')
print(*[el for el in get_factorial(num)])


