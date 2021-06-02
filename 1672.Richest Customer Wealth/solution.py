class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        tempList = []
        for i in accounts:
            temp = 0
            for j in i:
                temp += j
            tempList.append(temp)
        tempList.sort()
        return tempList[-1]
