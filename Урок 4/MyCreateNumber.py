# Модуль для шестого задания

from itertools import count


def create_number(start_num, end_num = 5):
    for i in count(start_num):
        if i > end_num:
            break
        yield i
