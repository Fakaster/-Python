def divide(a, b):
    return a / b


while True:
    a = input("Введите числитель ")
    b = input("Введите знаменатель ")
    if a.isdigit() and b.isdigit() and int(b) != 0:
        break

print(f"Результатом деления {a} на {b} будет {divide(int(a), int(b))}")
