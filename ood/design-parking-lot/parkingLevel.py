class ParkingLevel:
    def __init__(self, floor):
        self.__floor = floor
        self.__motorcycle_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}

    