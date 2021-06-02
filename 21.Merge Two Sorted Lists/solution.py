class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create new linked list, head so we can leave a pointer there to return
        temp_list = head = ListNode(0)
        # While both linked lists have a value
        while l1 and l2:
            # If l1 value less than l2 value
            if l1.val < l2.val:
                # Add l1 value to temp list
                temp_list.next = l1
                # Go to next l1 value
                l1 = l1.next
            # If l2 value less than l1 value
            else:
                # Add l2 value to temp list
                temp_list.next = l2
                # Go to next l2 value
                l2 = l2.next
            # Iterate to next temp list item
            temp_list = temp_list.next
        # If l2 still has items
        if l1 == None:
            # Add l2 to temp list
            temp_list.next = l2
        # If l1 still has items
        else:
            # Add l1 to temp list
            temp_list.next = l1
        # Return temp list
        return head.next
