class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0 and num != 1:
            while (num % 2) == 0:
                num = num/2
                counter += 1
            num -= 1
            counter += 1
        return counter
