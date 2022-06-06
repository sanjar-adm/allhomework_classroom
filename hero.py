from random import choice, randint


class Hero:
    def __init__(self, level, name):
        self.__level = level
        self.__name = name

    def __str__(self):
        return str(self.__name)

    def level_up(self):
        self.__level += 1
        return self.__level


class Soldier(Hero):
    def __init__(self, name_of_hero=None):
        self.__name_of_hero = name_of_hero

    def follow_the_hero(self):
        print(f'Иду за героем {self.name_of_hero}')

    def __str__(self):
        return str(f'Воин {self.__name_of_hero} c номером {id(self)}')


def main():
    list_of_hero = [Hero(1, 'Манас'), Hero(10, 'Семетей'), Hero(3, 'Кайрат')]
    list_of_army = [[] for i in range(len(list_of_hero))]

    for i in range(30):
        index_hero = randint(0, len(list_of_hero) - 1)
        list_of_army[index_hero].append(Soldier(list_of_hero[index_hero]))

    max = index = 0
    for i in range(0, len(list_of_army)):
        print(f'У героя {list_of_hero[i]} кол-во воинов {len(list_of_army[i])}')
        if max < len(list_of_army[i]):
            max = len(list_of_army[i])
            index = i

    print("\n***Результат**")
    print(f'Герой {list_of_hero[index]} выиграл!')
    print(f'У героя {list_of_hero[index]} повышается уровень на {list_of_hero[index].level_up()}')


if __name__ == '__main__':
    main()


