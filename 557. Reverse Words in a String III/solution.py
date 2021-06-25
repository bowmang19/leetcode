class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        s = s.split(' ')
        for word in s:
            output.append(word[::-1])
        return ' '.join(output)
