class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Get each unique item
        arrSet = set(arr)
        temp = []
        # For each unique item, append the number of occurences of it to a temp list
        for i in arrSet:
            temp.append(arr.count(i))
        # If the set of the number of occurences is equal to the len of the set of the original list, return true, otherwise return false
        return len(set(temp)) == len(arrSet)
