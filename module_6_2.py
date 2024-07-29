class Vehicle:
    __COLOR_VARIANTS = ['white', 'red', 'blue', 'black']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):

        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        lst = [s.lower() for s in self.__COLOR_VARIANTS]
        if new_color.lower() in lst:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle = Sedan('tom', 'geep', 'red', 100)

vehicle.print_info()

vehicle.set_color('BLACK')
vehicle.set_color('Pink')
vehicle.owner = 'Bob'

vehicle.print_info()
