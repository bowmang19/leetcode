class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            # Disregard first item
            if i == 0:
                continue
            if nums[i-1] >= nums[i]:
                dif = nums[i-1] - nums[i] + 1
                nums[i] += dif
                counter += dif
            continue
        return counter
