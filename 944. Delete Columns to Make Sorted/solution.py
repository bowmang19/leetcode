class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        index, output = 0, 0
        length = len(strs[0])
        while index != length:
            temp1, temp2 = [], []
            for word in strs:
                temp1.append(word[index])
                temp2.append(word[index])
            if temp1 != sorted(temp2):
                output += 1
            index += 1
        return output
