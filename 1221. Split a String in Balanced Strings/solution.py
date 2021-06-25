class Solution:
    def balancedStringSplit(self, s: str) -> int:
        output = 0
        balance = 0
        for i in s:
            if i == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                output += 1
        return output
