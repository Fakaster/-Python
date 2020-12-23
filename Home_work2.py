user_second = int(input('Введите время в секундах '))
h = user_second // 3600
m = user_second % 3600 // 60
s = user_second % 3600 % 60
print(f'ремя в формате чч:мм:сс {h}:{m}:{s}')
