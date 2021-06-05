class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        sortedHeights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                counter += 1
        return counter
