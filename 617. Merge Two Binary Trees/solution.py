# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # If there's not a node in root 1, return root 2 node
        if not root1:
            return root2
        # If there's not a node in root 2, return root 1 node
        if not root2:
            return root1
        # If both nodes, combine values and store in root1 tree
        root1.val += root2.val
        # Recursively call function on root1 and root2 left node
        root1.left = mergeTrees(root1.left, root2.left)
        # Recursively call function on root1 and root2 right node
        root1.right = mergeTrees(root1.right, root2.right)
        # Return root1 node when no child nodes at all (to pass you back up the tree)
        return root1
