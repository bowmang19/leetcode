class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        output = []
        for i in range(0, k):
            output.append(s[i])
        return " ".join(output)
