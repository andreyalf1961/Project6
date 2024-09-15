class Figure:
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return (all(isinstance(x, int) and x > 0 for x in new_sides) and len(new_sides) == self.sides_count)

    def set_sides(self, *new_sides):
        if isinstance(self, Cube) and len(new_sides) == 1:
            new_sides = [new_sides] * 12
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length):
        super().__init__(color, 1)
        self.__length = length
        self.__radius = length / (2 * 3.14)  # Approximating pi

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = list(sides)
        print(self.sides)

    def get_square(self):
        s = sum(self.sides) / 2
        return (s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *(sides * self.sides_count))
        self.sides = sides

    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# t = Triangle((222, 55, 100), 3, 4,5)
#
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# #
# # # Проверка на изменение сторон:
cube1.set_sides(5)
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# # # Проверка периметра (круга), это и есть длина:
print(len(circle1))
# #
# # # Проверка объёма (куба):
print(cube1.get_volume())

# print(t.get_square())
