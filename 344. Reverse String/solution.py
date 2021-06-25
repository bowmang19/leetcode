class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointer1, pointer2 = 0, len(s) - 1
        while pointer1 < pointer2:
            temp = s[pointer1]
            s[pointer1] = s[pointer2]
            s[pointer2] = temp
            pointer1 += 1
            pointer2 -= 1
