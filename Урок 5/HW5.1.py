txt = ''
with open("HomeWork1.txt", 'w') as f_obj:
    while True:
        txt = input()
        if txt == '':
            break
        f_obj.writeline(txt + "\n")
