low_pay = []
count_pay = 0
sum_pay = 0
res_avg = 0
with open("HomeWork3.txt") as f_obj:
    lst = [line.split() for line in f_obj]
    low_pay = [i[0] for i in lst if int(i[1]) < 20000]
    sum_pay = sum(int(i[1]) for i in lst)
    count_pay = sum(1 for i in lst)
print(f'Сотрудники с низкой зарплатой - {low_pay}')
print(f'Средняя зарплата составляет {sum_pay/count_pay}')



