class Car:
    def describe(self):
        return "This is a regular car"

class ElectricCar(Car):
    def describe(self):
        return "This is an electric car"

class Truck(Car):
    def describe(self):
        return "This is a heavy-duty truck"

# Tạo danh sách các xe khác nhau
vehicles = [Car(), ElectricCar(), Truck()]

# Duyệt qua từng xe và gọi describe()
for v in vehicles:
    print(v.describe())