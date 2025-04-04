class Car:
    def __init__(self, brand, color):
        self.__brand = brand  # Thuộc tính private (ẩn)
        self.__color = color  # Thuộc tính private (ẩn)

    # Getter: Lấy giá trị color
    def get_color(self):
        return self.__color

    # Setter: Thay đổi giá trị color
    def set_color(self, new_color):
        if new_color in ["red", "blue", "black"]:  # Kiểm tra hợp lệ
            self.__color = new_color
        else:
            print("Màu không hợp lệ!")

    def describe(self):
        return f"This is a {self.__color} {self.__brand} car"
class ElectricCar(Car):
    def __init__(self, brand, color, battery):
        super().__init__(brand, color)
        self.__battery = battery
    def describe(self):
        return f"This is a {self.get_color()} {self._Car__brand} car with {self.__battery} kWh battery"

#test
if __name__ == "__main__":
    car2 = ElectricCar("Tesla", "black", 100)
    print(car2.describe())