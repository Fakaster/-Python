lst = input('Введите значения для заполнения списка через пробел ').split()
end = len(lst)
sec = 0
if end != 1:
    for i in range(0, end, 2):
        sec = i // (end - 1)
        lst[i], lst[i + 1 - sec] = lst[i + 1 - sec], lst[i]
print(lst)
