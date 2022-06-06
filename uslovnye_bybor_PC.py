gb = 4 
ssd = 256 
hdd = 1000
money = 1000
type_of_hard_drive = 'SSD'
# if gb < 8 and ssd ==hdd == 1000:
if gb > 4 and gb < 8:
    if type_of_hard_drive == 'HDD' and  hdd >= 1000:
        if money <= 1000:
            print('Вам подходит!')
        elif money > 1000:
            print('Слишком дорого!')
    elif type_of_hard_drive == 'HDD' and  hdd < 1000:
        print('Нет не подходит!')
    elif type_of_hard_drive == 'SSD' and ssd >= 256:
        if money <= 1000:
            print('Вам подходит!')
        elif money > 1000:
            print('Слишком дорого!')
    elif type_of_hard_drive == 'SSD' and ssd < 256:
        print('Не подходит SSD! ')