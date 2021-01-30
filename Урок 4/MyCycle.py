# Модуль для шестого задания
from itertools import cycle


def show_list(lst, stop_num = 100):
    i = 0
    for el in cycle(lst):
        if i > stop_num:
            break
        yield el
        i += 1
