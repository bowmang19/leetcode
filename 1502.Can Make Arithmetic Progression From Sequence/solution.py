class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortList = sorted(arr)
        dif = sortList[0] - sortList[1]
        for i in range(len(sortList)):
            print(i)
            if i != len(sortList)-1:
                if dif != sortList[i] - sortList[i+1]:
                    return False
        return True
