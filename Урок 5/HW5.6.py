res = {}
lst = []
with open('HomeWork6.txt') as f_obj:
    lst = [n.split() for n in f_obj]
for i in range(len(lst)):
    res[lst[i][0]] = sum(int(i) for i in lst[i][1:])
print(f'{res}')
