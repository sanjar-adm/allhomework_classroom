class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying=False, is_land=False):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__max_speed = max_speed
        self.__odometer = odometer
        self.__is_flying = is_flying
        self.__is_land = is_land

    def take_off(self):
        self.__is_flying = True
        self.__is_land = False
        return 'Взлет...'

    def land(self):
        self.__is_flying = False
        self.__is_land = True
        return 'Приземление...'

    def fly(self, distance, new_odometer_value):
        self.__distance = distance
        self.__odometer = new_odometer_value
        return 'Летит...'

v1 = Airplane('Cobra', 'W-22', 2021, 620, 420)

print(v1.take_off())
print(v1.__dict__)

print(v1.fly('200km', 240))
print(v1.__dict__)

print(v1.land())
print(v1.__dict__)

