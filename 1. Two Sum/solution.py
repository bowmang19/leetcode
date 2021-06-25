
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in len(nums):
            for j in len(nums):
                if nums[i] + nums[j] == target and i != j:
                    if i not in solution and j not in solution:
                        solution.extend([i, j])
        return solution
