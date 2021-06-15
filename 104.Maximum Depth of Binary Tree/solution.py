# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # If there is no child node from previous recursion...
        if root == None:
            # ...do not add anymore depth
            return 0
        else:
            # Otherwise, return 1 added to the maximum value between the recursion of the left and right child node
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
