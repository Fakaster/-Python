from random import randrange

first_list = [randrange(20) for n in range(randrange(10, 25))]
print(f"Исходный список {first_list}")
res_list = [i for i in first_list if first_list.count(i) == 1]
print(f"Итоговый список {res_list}")
