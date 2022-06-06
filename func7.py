list_1 = [1,2,-3,4,-34,3,-3,-4,-2,-36,23,9]
def sort_list_number(l):
    positive_list = [i for i in l if i > 0]
    negative_list = [i for i in l if i < 0]
    return positive_list, negative_list

print(sort_list_number(list_1))