# Написал это задание с импортом своих скриптов (так понял)
# Если нужно было делать по другому, то код ниже

from MyCreateNumber import create_number
from MyCycle import show_list


lst = [i for i in create_number(3, 7)]
print(lst)
for el in show_list(lst, 25):
    print(el)

#Этот блок кода на тот случай, если задание нужно было делать в одном файле

# from itertools import count
# from itertools import cycle

# def create_number(start_num, end_num = 5):
#     for i in count(start_num):
#         if i > end_num:
#             break
#         yield i
#
# def show_list(list, stop_num = 100):
#     i = 0
#     for el in cycle(list):
#         if i > stop_num:
#             break
#         yield el
#         i += 1
#
# lst = [i for i in create_number(3, 7)]
# print(lst)
# for el in show_list(lst, 25):
#     print(el)