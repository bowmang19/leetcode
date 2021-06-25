# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.output = []
        self.inorder(root, low, high)
        return sum(self.output)

    def inorder(self, root: TreeNode, low: int, high: int):
        if root == None:
            return
        if root.val >= low and root.val <= high:
            self.output.append(root.val)
        self.inorder(root.left, low, high)
        self.inorder(root.right, low, high)
