My_dict = {'One': "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('HomeWork4.txt') as f_obj:
    lst = [i.split() for i in f_obj]
with open("NewHomeWork4.txt", 'w') as fw_obj:
     for el in lst:
         fw_obj.writelines(f'{My_dict[el[0]]} {el[1]} {el[2]}\n')
