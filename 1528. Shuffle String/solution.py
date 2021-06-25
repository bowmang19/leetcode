class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create placeholder list of necessary length
        placeholder = ['_'] * len(s)
        for i, j in zip(s, indices):
            # Replace placeholders in list with items in s
            placeholder[j] = i
        # Rejoin list into output string
        return ''.join(placeholder)
