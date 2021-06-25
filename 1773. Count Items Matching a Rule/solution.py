class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        tempNum = 0
        if ruleKey == 'type':
            for i in items:
                if i[0] == ruleValue:
                    tempNum += 1
        elif ruleKey == 'color':
            for i in items:
                if i[1] == ruleValue:
                    tempNum += 1
        else:
            for i in items:
                if i[2] == ruleValue:
                    tempNum += 1
        return tempNum
