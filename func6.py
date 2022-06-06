numbers = map(int,input('введите числа через пробел: ').split())
s = int(input('сдвиг: '))
def cesar(l,n):
    l = list(l)
    if n<0:
        n = abs(n)
        for i in range(n):
            l = l[1:]+l[:1]
    else:
        for i in range(n):
            l = l[-1:]+l[:-1]
    return l
print(cesar(numbers,s))