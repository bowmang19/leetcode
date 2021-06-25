class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # This is a horribly worded question
        comparison = []
        output = []
        print(target)
        for i in range(1, n + 1):
            if comparison == target:
                break
            comparison.append(i)
            output.append('Push')
            if i not in target:
                comparison.pop()
                output.append('Pop')
        return output
