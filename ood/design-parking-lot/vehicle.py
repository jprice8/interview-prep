from abc import ABC


class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__type = vehicle_type
        self.__ticket = ticket
        self.__parking_spots = []
        self.__spots_needed = 0

    def assign_ticket(self, ticket):
        self.__ticket = ticket 

    def getSpotsNeeded(self):
        return self.__spots_needed



class Bus(Vehicle):
    def __init__(self, license_number, vehicle_type, ticket=None):
        super().__init__(license_number, vehicle_type, ticket=ticket)    


class Car(Vehicle):
    def __init__(self, license_number, vehicle_type, ticket=None):
        super().__init__(license_number, vehicle_type, ticket=ticket)


class Motorcycle(Vehicle):
    def __init__(self, license_number, vehicle_type, ticket=None):
        super().__init__(license_number, vehicle_type, ticket=ticket)
