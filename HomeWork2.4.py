lst = input('Введите  строку из нескольких слов ').split()
n = 1
for i in lst:
    print(f'{n} - {i[:10]}')
    n += 1
