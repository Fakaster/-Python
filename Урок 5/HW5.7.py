import json


profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('HomeWork7.txt') as fw_obj:
    for line in fw_obj:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Средняя прибыль отсутствует')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('HomeWork7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Итоговый json файл с данными: \n '
          f' {js_str}')