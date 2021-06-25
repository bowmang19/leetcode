class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        output = 0
        for i in range(0, len(s) - 2):
            # Check if there are 3 unique letters next to each other
            if len(set(s[i:i+3])) == 3:
                output += 1
        return output
