class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomList = []
        for i in range(0, len(nums), 2):
            for _ in range(1, nums[i] + 1):
                decomList.append(nums[i + 1])
        return decomList
