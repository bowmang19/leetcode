class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:length + i] == needle:
                return i
        return -1
