class Figure:
    def __init__(self,  __sides,  __color, sides_count=0, filled=None):
        self.__sides = __sides
        self.__color = __color
        self.sides_count = sides_count



    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = []
            self.__color = [r, g, b]
        else:
            self.__color = self.__color





    def __is_valid_sides(self, *args):
        self.args = args
        k = 0
        if len(args) == len(self.__sides):
            for i in args:
                if i == int(i) and i > 0:
                    k += 1
        if k == len(args):
            return True
        else:
            return False


    def get_sides(self):
        return self.__sides


    def __len__(self):
        sum_ = 0
        for i in self.__sides:
            sum_ += i
        return sum_


    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            self.__sides = self.__sides
        else:
            self.__sides = []
            for i in new_sides:
                self.__sides.append(i)






class Circle(Figure):
    sides_count = 1

    def __init__(self, color, lens):
        self.color = color
        self.lens = lens
        Figure.sides_count = 1
        super().__init__([lens], color, self.sides_count)
        self.__radius = lens/(2*3.14)





    def get_square(self):
        return 3.14*(self.__radius**2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, lens):
        self.color = color
        self.lens = lens
        super().__init__([self.lens for lens in range(12)], color, self.sides_count)


    def get_volume(self):
        return self.lens**3



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        self.color = color
        self.args = args

        if len(args) != self.sides_count:
            self.args = [1, 1, 1]
            super().__init__([1, 1, 1], color, self.sides_count)
        else:
            super().__init__(args, color, self.sides_count)
        self.pp = super().__len__()/3
        self.__height = (self.pp * (self.pp-self.args[0]) * (self.pp-self.args[1]) * (self.pp-self.args[2]))**0.5



    def get_square(self):
        self.S = 0.5*self.args[0]*self.__height
        return self.S




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
Triangle1 = Triangle((222, 35, 130), 6,6,3)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
Triangle1.set_color(255, 255, 255) # Изменится
print(Triangle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
Triangle1.set_sides(3,2,1) # Изменится
print(Triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка для площади (треугольника):
print(Triangle1.get_square())