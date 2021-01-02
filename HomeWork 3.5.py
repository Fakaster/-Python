res = 0
flag = True
while flag:
    lst = input("Введите числа через пробел, символ ! завершает выполнение ").split()
    for i in lst:
        if i.isdigit():
            res += int(i)
        elif i == "!":
            flag = False
    print(f"Сумма введенных чисел = {res}")

