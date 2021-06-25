# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string = ''
        while(True):
            string += str(head.val)
            if head.next == None:
                break
            head = head.next
        return int(string, 2)
