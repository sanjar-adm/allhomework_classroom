# class Abonent:
#     def __init__(self,
#                  identification_number, surname, name, middle_name, address, credit_card_number, debit, credit, time_of_long_distance_and_city_negotiations
# ):
#         self.identification_number = identification_number
#         self.surname = surname
#         self.name = name
#         self.middle_name = middle_name
#         self.address = address
#         self.credit_card_number = credit_card_number
#         self.debit = debit
#         self.credit = credit
#         self.time_of_long_distance_and_city_negotiations = time_of_long_distance_and_city_negotiations
#
#     def get_info(self):
#         return self.surname
#
# exmp = Abonent(1, 1, 1, 1, 1, 1, 1, 1, 1)
#
# print(exmp.get_info())


# class MyStr:
#
#     def __init__(self, some_string):
#         self.some_string = some_string
#
#     def count(self, pattern):
#         elements = dict()
#         for elem in self.some_string.lower():
#             if elem not in elements:
#                 elements[elem] = 1
#             else:
#                 elements[elem] += 1
#
#         return elements[pattern]
#
#
# word = str("ErlanR")
# print(word.count('r'))
#
# word = MyStr("ErlanR")
# print(word.count('r'))

class Abonent:
    def __init__(self,
                 identification_number, surname, name, middle_name, address, credit_card_number, debit, credit, time_of_long_distance_and_city_negotiations
):
        self.identification_number = identification_number
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.address = address
        self.credit_card_number = credit_card_number
        self.debit = debit
        self.credit = credit
        self.time_of_long_distance_and_city_negotiations = time_of_long_distance_and_city_negotiations

    def set_value(self, identification_number, surname, name, middle_name):
        self.identification_number = identification_number
        self.surname = surname
        self.name = name
        self.middle_name = middle_name

    def get_info(self):
        return self.name

exmp = Abonent(1, 'sanjar', 'sanjar', 'sanjar', 'awd', 123, 'no', 'no', 'awdawd', )

print(exmp.get_info())
exmp.set_value(2, 'NewSanjar', 'Sanjar2', 'MiddleSan')

print(exmp.get_info())



