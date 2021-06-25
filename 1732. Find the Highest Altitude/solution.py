class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        max = 0
        for i in gain:
            sum += i
            if sum > max:
                max = sum
        return max
