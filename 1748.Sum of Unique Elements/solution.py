class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        temp = {}
        sum = 0
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i in temp.keys():
            if temp[i] == 1:
                sum += i
        return sum
