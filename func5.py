dict_one = {'a':1, 'b':2, 'c':3}
dict_two = {'d':4, 'e':5, 'f':6}
dict_three = {'g':7, 'h':8, 'i':9}
dict_four = {}
t = zip(dict_one,dict_two,dict_three)
for a,b,c in t:
    dict_four[a] = dict_one[a]
    dict_four[b] = dict_two[b]
    dict_four[c] = dict_three[c]
print(dict_four)