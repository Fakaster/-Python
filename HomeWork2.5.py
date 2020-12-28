lst = [4, 5, 11, 7, 5, 5]
lst.sort(reverse=True)

while True:
    print(f'Текущий рейтинг - {lst}')
    lst.append(int(input('Введите число для добавлени в рейтинг ')))
    lst.sort(reverse=True)
