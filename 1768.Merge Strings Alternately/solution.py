class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        i = 0
        while i < len(word1) and i < len(word2):
            output += word1[i]+word2[i]
            i += 1
        return output+word1[i:]+word2[i:]
