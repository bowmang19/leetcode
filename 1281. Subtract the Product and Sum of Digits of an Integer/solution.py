class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multN = 1
        sumN = 0
        for i in str(n):
            multN *= int(i)
            sumN += int(i)
        return multN - sumN
