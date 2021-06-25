class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        maxUnits = 0
        for i in boxTypes:
            for j in range(i[0]):
                if truckSize != 0:
                    maxUnits = maxUnits + i[1]
                    truckSize = truckSize - 1
                else:
                    break
        return maxUnits
