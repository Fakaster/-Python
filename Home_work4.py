n = input("Введите число n ")
i = 0
max_n = 0

while i in range(len(n)):
    if max_n < int(n[i]):
        max_n = int(n[i])
    i += 1
print(max_n)
