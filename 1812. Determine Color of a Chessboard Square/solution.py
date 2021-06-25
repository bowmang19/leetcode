class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coordinates = list(coordinates)
        convertedCoord = (ord(coordinates[0]) - 96)
        combined = convertedCoord + int(coordinates[1])
        if combined % 2 == 0:
            return False
        return True
