class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num = str(x)
            num = int(num[::-1])
            if num == x:
                return True
            else:
                return False
