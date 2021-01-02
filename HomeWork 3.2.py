def user_info(name, surname, year_birth, city, email, phone):
    print(f"А речь пойдет о человеке которого звали {name} {surname}."
          f"\nРодился он в {year_birth} году, в славном городке под названием {city}"
          f"\nЕсли вам интересен данный человек то вот его номер телефона {phone} и его email {email}")


name = input("Введите имя ")
surname = input('Введите фамилию ')
year_birth = input('Введите год рождения ')
city = input('Введите город ')
email = input('Введите email ')
phone = input('Введите номер телефона ')
user_info(name, surname, year_birth, city, email, phone)