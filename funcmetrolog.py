def bank(m, y):
    first_year = m / y
    final = 0
    p = 0, 1
    for i in range(y):
        final += first_year
        first_year += first_year * 0.1
    return final
m = int(input('Введите вклад :'))
years = int(input('Введите срок :'))
print(bank(m,years))
