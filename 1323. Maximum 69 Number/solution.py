class Solution:
    def maximum69Number(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        for i in range(len(num)):
            if num[i] == 6:
                num[i] = 9
                break
        numStr = [str(integer) for integer in num]
        numJoined = "".join(numStr)
        num = int(numJoined)
        return num

        '''
        Can only change one digit

        '''
