def my_func(a, b, c):
    return max(a, b, c) + ((a + b + c) - max(a, b, c) - min(a, b, c))


a, b, c = int(input('Введите число ')), int(input('Введите число ')), int(input('Введите число '))
print(f"Сумма наибольших чисел = {my_func(a, b, c)}")