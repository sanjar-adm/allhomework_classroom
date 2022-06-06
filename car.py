class Car:
    def __init__(self, make, model, year, fuel=70, odometer=0):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__fuel = fuel
        self.__odometer = odometer

    def __add_distance(self, distance):
        self.__odometer += distance

    def __subtract_fuel(self):
        self.__fuel -= (self.__fuel * 10) / 10

    def drive(self, distance):
        if self.__fuel * 10 >= distance:
            self.__add_distance(distance)
            self.__subtract_fuel()
            print("Let's drive!")
        else:
            print("Need more fuel, please, fill more!")


v1 = Car('Merc', 'w222', '2018', 9, 0)
v1.drive(100)