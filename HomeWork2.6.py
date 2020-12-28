lst = []
my_dict = dict()
res_dict = {'название': [], 'цена': [], 'количество': [], 'eд': []}
res_lst = []

for i in range(3):
    my_dict['название'], my_dict['цена'], my_dict['количество'], my_dict['eд'] = \
        input('Введите название, цену, кол-во, ед. измерения ').split()
    lst.append((i + 1, my_dict.copy()))
#print(lst)

for i in my_dict.keys():
    for n in lst:
        res_dict[i].append(n[1][i])
    #Добавляю эти две строки что бы соответствовать примеру задания
    #значения в итоге не повторяются (по "шт" видно)
    #и представлены списком
    res_dict[i] = set(res_dict[i])
    res_dict[i] = list(res_dict[i])
print(res_dict)


