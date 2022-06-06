file = input('Введите название файла  :')
if '.' in file:
    a = file.split(".")
    print('Ваше расширение', a[1])
else:
    print('Нету расширения! ')  