class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        output = ''
        for i in s:
            if i == '(':
                counter += 1
            if counter > 1:
                output += i
            if i == ')':
                counter -= 1
        return output
