class Solution:
    def maxDepth(self, s: str) -> int:
        maximum, counter = 0, 0
        for i in s:
            if i == '(':
                counter += 1
                if counter > maximum:
                    maximum = counter
            if i == ')':
                counter -= 1
        return maximum
