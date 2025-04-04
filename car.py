class Car:
    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def describe(self):
        return f"This is a {self.__color} {self.__brand} car"