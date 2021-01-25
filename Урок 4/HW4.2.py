from random import randrange

first_list = [randrange(500) for n in range(randrange(10, 25))]
res_list = []
print(first_list)
temp = first_list.pop(0)
for i in first_list:
    if i > temp:
        res_list.append(i)
    temp = i
print(res_list)