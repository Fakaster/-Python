from random import randrange

first_list = [str(randrange(20))for n in range(randrange(2, 5))]
with open("HomeWork5.txt", 'w')as fw_obj:
    for i in first_list:
        fw_obj.write(i + " ")
with open("HomeWork5.txt")as fr_obj:
    pr = fr_obj.read().split()
    res = sum(int(i) for i in pr)
print(f'Сумма чисел из файла = {res}')
