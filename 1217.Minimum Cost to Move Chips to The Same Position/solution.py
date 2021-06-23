class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Free to move even to even or odd to odd
        # So you can move all the chips next to each other for free
        # The cost will be the minimum number between the num of even and num of odd chips
        even, odd = 0, 0
        for chip in position:
            if chip % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
