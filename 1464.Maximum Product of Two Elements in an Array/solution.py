class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(nums)):
            if nums[i] > first:
                first = nums[i] - 1
                firstIndex = i
        for j in range(len(nums)):
            if nums[j] > second and j != firstIndex:
                second = nums[j] - 1
        return first * second
