from abc import ABC, abstractmethod

class Vehicle(ABC):
    total_vehicles = 0

    def __init__(self, speed, capacity):
        self._speed = speed
        self.__capacity = capacity
        Vehicle.total_vehicles += 1

    @staticmethod
    def get_total_vehicles():
        return Vehicle.total_vehicles

    @abstractmethod
    def move(self):
        pass

    def get_capacity(self):
        return self.__capacity

    def vehicle_info(self):
        return f"Speed: {self._speed} km/h, Capacity: {self.__capacity} persons"

class Car(Vehicle):
    def __init__(self, speed, capacity, fuel_type):
        super().__init__(speed, capacity)
        self.fuel_type = fuel_type

    def move(self):
        if self.fuel_type == "electric":
            return f"The car moves silently at {self._speed} km/h."
        else:
            return f"The car moves with an engine sound at {self._speed} km/h."

    def vehicle_info(self):
        return f"Car -> Speed: {self._speed} km/h, Capacity: {self.get_capacity()} persons, Fuel type: {self.fuel_type}"

class Bicycle(Vehicle):
    def __init__(self, speed, capacity, has_gears):
        super().__init__(speed, capacity)
        self.has_gears = has_gears

    def move(self):
        if self.has_gears:
            return f"The bicycle with gears moves at {self._speed} km/h."
        else:
            return f"The simple bicycle moves at {self._speed} km/h."

    def vehicle_info(self):
        gears_info = "with gears" if self.has_gears else "without gears"
        return f"Bicycle -> Speed: {self._speed} km/h, Capacity: {self.get_capacity()} persons, {gears_info}"

car = Car(120, 5, "gasoline")
bicycle = Bicycle(25, 1, True)

print(car.move())
print(bicycle.move())
print(car.vehicle_info())
print(bicycle.vehicle_info())
print(f"Total vehicles created: {Vehicle.get_total_vehicles()}")
