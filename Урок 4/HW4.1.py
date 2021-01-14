from sys import argv

script_name, worked_hour, cost_hour, prize = argv
print(f"Общая выроботка в часах = {worked_hour}")
print(f"Ставка в час = {cost_hour}")
print(f"Премия = {prize}")
print(f"Заработная плата сотрудника составляет {int(worked_hour) * int(cost_hour) + int(prize)}")
