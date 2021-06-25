class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ''
        for i in range(len(s)):
            if i % 2 != 0:
                output = output + (chr(ord(s[i-1]) + int(s[i])))
                continue
            output += s[i]
        return output
