price = 10000
name_car = 'Lexus'
year_car = 2004
km = 150000
color = 'white grey'
rul = 'left'
if name_car == 'Toyota' or name_car == 'Lexus':
    if rul == 'left':
        if year_car >= 2004:
            if km <= 150000:
                if price <= 10000:
                    print('Самый топовый вариант!')
                else:
                     print('Слишком дорого!')
            elif km == 200000:
                if price < 8000:
                    print('Идеально!')
                else:
                    print('Слишком дорого для своего пробега!')
            else:
                print('Пробег слишком большой!')
        else:
            print('Машина слишком старая')
    else:
        print('Праворульный не подходит!')
else:
    print('Модель машины не подходит!')