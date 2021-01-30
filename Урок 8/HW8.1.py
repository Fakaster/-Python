class Date:
    _date = ''

    def __init__(self, date: str):
        Date._date = date

    @classmethod
    def date_to_num(cls):
        ls = list(map(int, Date._date.split('-')))
        return ls

    @staticmethod
    def check_date(date: str or list):
        _date = date
        if isinstance(date, list):
            if 0 < _date[0] <= 31 and 0 < _date[1] <=12:
                return True
            else:
                return False
        else:
            _date = list(map(int, date.split('-')))
            return Date.check_date(_date)


Date(input("Введите дату в формате 'день-месяц-год' "))
test = Date.date_to_num()
[print(f"{i} является числов? - {isinstance(i, int)}") for i in test]
print(f'Введенная дата соответствует теребованиям? - {Date.check_date(test)}')
# print(Date.date_to_num())
11