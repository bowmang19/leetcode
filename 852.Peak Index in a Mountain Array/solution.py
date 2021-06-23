class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Binary search solution
        low = 0
        high = len(arr) - 1
        return self.findMaximum(low, high, arr)

    def findMaximum(self, low, high, arr):
        # Find midpoint
        mid = (low + high) // 2
        # Check if mid is the peak, if so return the mid index
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        # Check if item at mid index is greater than the next index item and less than the previous index item
        # Make high index - 1 our midpoint (get rid of upper half that doesn't have the peak)
        if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
            return self.findMaximum(low, mid - 1, arr)
        else:
            # Otherwise make low index + 1 our midpoint (get rid of bottom half that doesn't have peak)
            return self.findMaximum(mid + 1, high, arr)
