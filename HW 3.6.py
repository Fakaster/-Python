def int_func(lst_txt):
    lst_res = []
    for i in lst_txt:
        lst_res.append(i.capitalize())
    return lst_res

print(*int_func(input('Введите слова через пробел ').split()))
