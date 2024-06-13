class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            if self.big < 0: return False

        elif carType == 2:
            self.medium -= 1
            if self.medium < 0: return False

        else:
            self.small -= 1
            if self.small < 0: return False

        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)