class Animal:
    alive = True  # живой
    fed = False  #

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name



class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible=True

if __name__ == '__main__':

    a1 = Predator('волк')
    a2 = Mammal('ослик')
    p1 = Flower('аконит')
    p2 = Fruit('ананас')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
