# 1
a = 2**3
b = 3**2
if a>b:
    print('a меньше чем b')
else:
    print('b больше чем a')
# 2 
a = 34
b = 7
c = 101
if a>b:
    print('a>b')
elif b>c:
    print('b>c')
else:
    print('условие не верно!')

# 3 
a = 17391 % 17
b = 546 % 17
c = 934 % 17
if a < b and a < c :
    print('остаток меньше в a')
elif b < a and b < c:
    print('остаток меньше в b')
elif c < b and c < a:
    print('остаток меньше в с')
else:
    print('НЕТ остатка') 
   
# 4 
x = 13**2
if x == 172:
    print('Условие верно!')
else:
    print(x**2)

# 5 
x = int(input('Введите число :'))
if x % 2 == 0:
    print('x четное')
if x % 3 == 0:
    print('x делится без остатка')
if (x ** 2) > 1000:
    print(' меньше 1000')
else:
    print('ты не на правильном пути')

# 6 

x = int(input('Введите число :'))
if 0 > x < 21 or 57 > x < 100:
    print('Разрешен')
else:
    print('Запрещен')

# 7 
x = True
if x == True:
    print('True')
# 8
today_weather = 'Sunny'
is_glasses = True

if today_weather == "Sunny":
    print('Taday not bad weather')
    if is_glasses:
        print("you cool boy!")
    else:
        print("go to home!")

# 9 
a = 10//5
b = 10/5
if a == b :
    print('a и b равны')
else:
    print(a+b)

# 10

x = int(input('ВВЕДИ ЧИСЛО :'))
if x > 0:
    print(x)
else:
    print(-x)

# 11 
a = 10 
b = 5 
if a == True and b ==True:
    print('У вас положительное число')

