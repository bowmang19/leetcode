class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Create temp array to return
        tempArray = []
        # Iterate through range of length of the array
        for i in range(len(nums)):
            # Insert the num at said index in the range in the temp array
            tempArray.insert(index[i], nums[i])
        # Return the temp array
        return tempArray
