class Solution:
    def defangIPaddr(self, address: str) -> str:
        tempStr = ''
        for i in address:
            if i == '.':
                tempStr = tempStr + '[' + '.' + ']'
            else:
                tempStr += i
        return tempStr
