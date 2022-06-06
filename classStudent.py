class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return self.name + '' + self.lastname + 'поступил в ' + self.year_of_entrance + 'на факультет' + self.department

data = Student('Автандил' , 'Курбанов', 'программирование листкампрехеншн','2017 году до нашей Эры.')
data.get_student_info()
print(data.get_student_info())

class Student:
    name = 'Avtandil'
    lastname = 'Kurbanov'
    department = 'Programm maker'
    def get_student_info(self):
        return self.name + '' + self.lastname + 'поступил' + self.year_of_entrance + 'на факультет' + self.department

    data = Student()
    print(data.get_student_info())