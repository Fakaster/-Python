class TestError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


a = int(input('Введите делимое '))
while True:
    b = int(input('Введите делитель '))
    try:
        if b == 0:
            raise TestError("Вы ввели ноль, на ноль делить нельзя")
    except TestError as err:
        print(err)
    else:
        break
print(a / b)
