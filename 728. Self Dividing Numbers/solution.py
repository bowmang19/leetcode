class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right + 1):
            lyst = [int(k) for k in str(i)]
            correct = []
            for j in lyst:
                if j == 0:
                    break
                if i % int(j) == 0:
                    correct.append(j)
            if correct == lyst:
                output.append(i)
        return output
