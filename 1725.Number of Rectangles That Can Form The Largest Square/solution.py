class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        counter = 0
        maxLen = 0
        for rectangle in rectangles:
            minSide = min(rectangle[0], rectangle[1])
            if minSide > maxLen:
                maxLen = minSide
        for rectangle in rectangles:
            if rectangle[0] >= maxLen and rectangle[1] >= maxLen:
                counter += 1
        return counter
