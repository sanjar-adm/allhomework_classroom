# Сформировать
# из введенного числа обратное по порядку входящих в него цифр и вывести
# на экран. Например, если введено число 3486, то надо вывести число 6843

a = int(input('Введите любое число :'))
n2 = 0
while a > 0:
    digit = a % 10
    a = a // 10
    n2 = n2 * 10
    n2 = n2 + digit
print('Обратное ему число:', n2)