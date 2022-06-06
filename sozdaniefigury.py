print('*\n**\n***\n****\n*****')
print('*\n**\n***\n****\n*****\n****\n***\n**\n*')
for i in range(1, 4):
    print(*['*']*i)
for i in range(2, 0, -1):
    print(*['*']*i)

n = 52
for i in range(n):
    x = int(i ** .5 + .5)
    k = x + 1 - abs(i - 1 - x ** 2)
    print('* ' * k)