#1
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
months_a.add("December")
a = months_a.union(months_b)
print(a)
for months in a:
    print(months.capitalize())

#2
x = {1, 2, 3}
y = {4, 3, 6}
print( x & y)