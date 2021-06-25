class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maximum
            if temp > maximum:
                maximum = temp
        arr[-1] = -1
        return arr
