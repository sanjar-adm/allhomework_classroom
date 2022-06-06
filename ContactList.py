class ContactList(list):
    def __init__(self, *names):
        self.__names = names

    def search_by_name(self, name):
        return [i for i in self.__names if name == i]

myList = ContactList('Sanjar', 'Avtandil', 'Kairat', 'Sanjar')
print(myList.search_by_name('Sanjar'))
