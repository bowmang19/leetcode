class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolList = []
        maxCandies = max(candies)
        for i in candies:
            if maxCandies <= i + extraCandies:
                boolList.append(True)
            else:
                boolList.append(False)
        return boolList
