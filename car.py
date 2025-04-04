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

car1 = Car("Toyota", "red")
print(car1.get_color())  # Output: red
car1.set_color("blue")   # Đổi màu hợp lệ
print(car1.get_color())  # Output: blue
car1.set_color("yellow") # Màu không hợp lệ!