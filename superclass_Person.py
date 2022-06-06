class Person :
    def __init__(self,name: str, age: str):
        self.name = name
        self.age = age

    def display(self):
        print(f'меня зовут {self.name} и мне сейчас {self.age} лет')

class Student(Person):
    def display_student(self):
        super().display()

student = Student('Автандил', '25')
student.display()
student.display_student()