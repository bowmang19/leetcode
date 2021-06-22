class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        words = [firstWord, secondWord, targetWord]
        summation = 0
        for i in range(len(words)):
            if i < 2:
                total = ''
                for j in words[i]:
                    total += str(ord(j) - 97)
                summation += int(total)
            else:
                targetTotal = ''
                for j in words[i]:
                    targetTotal += str(ord(j) - 97)
        return summation == int(targetTotal)
