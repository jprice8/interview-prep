from enum import Enum


class CarType(Enum):
    BIG = 1
    MEDIUM = 2 
    SMALL = 3


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        # dec
        if self.spots[carType - 1] > 0:
            self.spots[carType - 1] -= 1
            return True
        # ret
        return False



if __name__ == '__main__':
    ps = ParkingSystem(1, 1, 0)
    print(ps.addCar(1))