class Solution:
    def sortSentence(self, s: str) -> str:
        sList = s.split(' ')
        for i in range(len(sList)):
            sList[i] = sList[i][::-1]
        sList.sort()
        for i in range(len(sList)):
            sList[i] = sList[i][::-1]
            sList[i] = sList[i][0:-1]
        return ' '.join(sList)
