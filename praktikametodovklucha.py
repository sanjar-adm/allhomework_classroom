dict1 = {'a': 5,
         'b': 3,
         'c': 8,
         'd': 14}
for k , v  in dict1.items():
    print(k ,v )
    if v % 3 == 0:
        print('Hi')
    if v % 5 == 0:
        print('Bye')
