def mult(a,b):
    r = a*b
    def inner(c,d):
        return r + c/d
    return inner(a,b)
a  = int(input('Введите первое число :'))
b = int(input('Введите второе число :'))

print(mult(a,b))