count_line = 0
with open("HomeWork2.txt") as f_obj:
    count_line = sum(1 for line in f_obj)
    f_obj.seek(0)
    [print(f'Кол-во слов в строке =  {len(i.split())}') for i in f_obj]

print(f'Всего строк {count_line}')
