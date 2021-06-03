class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        completeWord1 = ''
        completeWord2 = ''
        for i in word1:
            completeWord1 += i
        for i in word2:
            completeWord2 += i
        if completeWord1 == completeWord2:
            return True
        return False
