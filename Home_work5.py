proceeds = int(input('Введите выручку '))
cost = int(input("Введите издержки "))
personnel = int(input("Введите кол-во сотрудников "))

fin_result = proceeds - cost
if fin_result > 0:
    print('Выручка больше издержек')
    print(f"Рентабельность {proceeds / cost * 100:.1f} %")
    print(f'Прибыль на одного сотрудника : {fin_result / personnel:.1f}')
else:
    print('Издержки больше выручки')
