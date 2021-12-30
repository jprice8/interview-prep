from enum import Enum
from abc import ABC


class ParkingSpotType(Enum):
    MOTORCYCLE, COMPACT, LARGE = 1, 2, 3


class Vehicle(ABC):
    def __init__(self, license_number):
        self.__license_number = license_number
    