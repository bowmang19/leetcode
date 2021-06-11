class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            # Disregard first item
            if i == 0:
                continue
            while nums[i] <= nums[i-1]:
                nums[i] += 1
                counter += 1
            continue
        return counter
