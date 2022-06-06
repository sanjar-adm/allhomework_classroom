print(""""Выберите действие:
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход """)
a = int(input('Выберите действие 1,2,3,4,5:  '))
list_of_cities = []
if a == 1:
    b = input('Введите название города  :')
    list_of_cities.append(b)
if a == 2:
    print(list_of_cities)
if a == 3:
    b = input('Введите новый город :')
    b1 = input('Введите город который хотите заменить :')
    if b1 in list_of_cities:
        list_of_cities.insert(b1, b)
    else:
        print('В списке не такого города')
if a == 4:
    b = input('Введите название  города :')
    if b in list_of_cities:
        list_of_cities.remove(b)
    else:
        print('В списке нет такого города! ')
if a == 5:
    print('Завершение работы!')



