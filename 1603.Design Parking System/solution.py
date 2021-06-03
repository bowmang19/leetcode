class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Initialize spot variables
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        # If carType is big and there is a spot, remove a spot and return True
        if carType is 1 and self.big > 0:
            self.big = self.big - 1
            return True
        # If carType is medium and there is a spot, remove a spot and return True
        elif carType is 2 and self.medium > 0:
            self.medium = self.medium - 1
            return True
        # If carType is small and there is a spot, remove a spot and return True
        elif carType is 3 and self.small > 0:
            self.small = self.small - 1
            return True
        # If no spot for the size, return false
        return False
