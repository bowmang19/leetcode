# Can't use python's lower() function
class Solution:
    def toLowerCase(self, s: str) -> str:
        asciiList = []
        for i in s:
            if ord(i) < 91 and ord(i) > 64:
                asciiList.append(chr(ord(i) + 32))
            else:
                asciiList.append(i)
        return "".join(asciiList)
