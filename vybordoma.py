price_house = 60000
building_materials  = 'Степень'
plot_size = '4 сотки'
if price_house < 50000 or price_house < 45000:
    print('Цена подходит')
else:
    print('цена не подходит!')
    if building_materials == 'Кирпич' or building_materials == 'Пескоблок':
        print('Материал подходит!')
    else:
        print('материал не подходит!')
        if plot_size == '4 сотки' or price_house == '5 соток':
            print('Размер участка подходит!')
        else:
            print('Размер участка не подходит!')
