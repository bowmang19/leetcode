class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for row in image:
            row.reverse()
            inverse = []
            for i in row:
                if i == 1:
                    inverse.append(0)
                else:
                    inverse.append(1)
            output.append(inverse)
        return output
