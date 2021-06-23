class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        pointer1, pointer2 = 0, 1
        # While our second pointer is less than the length of the array
        while pointer2 < len(nums):
            # If our odd pointer points to an even number...
            if nums[pointer2] % 2 == 0:
                # ... switch our values at odd and even (making sure our even pointer is now even)
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                # Move our even pointer to the next even index to potentially be switched
                pointer1 += 2
            else:
                # If our odd pointer is pointed at an odd number, iterate to next odd index to be checked
                pointer2 += 2
        return nums
