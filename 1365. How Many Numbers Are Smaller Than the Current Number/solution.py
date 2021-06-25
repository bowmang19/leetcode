class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tempArray = []
        for i in nums:
            counter = 0
            for j in nums:
                if i != j and i > j:
                    counter += 1
            tempArray.append(counter)
        return tempArray
