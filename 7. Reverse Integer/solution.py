class Solution:
    def reverse(self, x: int) -> int:
        solution = 0
        if x < 0:
            negative = True
            x = x * -1
        else:
            negative = False
        while x > 0:
            remainder = x % 10
            solution = (solution * 10) + remainder
            x = x // 10
        if negative == True:
            solution = solution * -1
        if solution <= ((2**31) - 1) and solution >= ((-2)**31):
            return solution
        else:
            return 0
