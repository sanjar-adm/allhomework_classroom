# Создать программу по подсчету суммы депозита:
#
# Вносим ежемесячную плату раз в месяц. Максимум 12 месяцев. Максимальная
# сумма 100000. Каждые 6 месяцев увеличиваем общую сумму на 10 процентов.
#
# В конце вывести сумму процентов и общую сумму

x = float(input("Введите сумму вклада: "))
month_h = 12

for i in range(12):
    if i > 6:
        i * 12
    x += x * 0.07
print(round(x, 2))