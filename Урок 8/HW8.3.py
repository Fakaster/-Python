class MyError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


lst = []
el = ''
while el != "stop":
    el = input('Введите число для добавления его в список ')
    try:
        if el.isnumeric():
            lst.append(int(el))
        else:
            raise MyError("Введено не число")
    except MyError as err:
        print(err)
print(f"Вы ввели слово stop, итоговый список - {lst}")
