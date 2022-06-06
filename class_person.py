class Person:
    full_name = None
    age = None
    place = None

    def __init__(self, full_name, place, age=18):
        self.full_name = full_name
        self.age = age
        self.place = place

    def talk(self):
        print(f"какой - то{self.full_name} говорит")

    @classmethod
    def move(cls, adress):
        cls.place = adress

    def __str__(self):
        return f'{self.full_name}{self.place}{self.age}'


p1 = Person('Sanzhar', 'BISHKEK', 18)
p1.talk()
print(p1)
