class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        leftPointer = 0
        rightPointer = len(nums) - 1
        while leftPointer < rightPointer:
            if nums[leftPointer] % 2 == 1 and nums[rightPointer] % 2 == 0:
                nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
                leftPointer += 1
                rightPointer -= 1
            if nums[leftPointer] % 2 == 0:
                leftPointer += 1
            if nums[rightPointer] % 2 == 1:
                rightPointer -= 1
        return nums
