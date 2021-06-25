class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tempArray = []
        tempArray.append(nums[0])
        for i in range(1, len(nums)):
            tempArray.append(nums[i] + tempArray[i-1])
        return tempArray
