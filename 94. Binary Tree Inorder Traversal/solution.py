# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive solution
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.output = []
        self.inorder(root)
        return self.output

    def inorder(self, root: TreeNode):
        # Check if the node is empty (and therefor has no child nodes)
        if root == None:
            return
        # Call function on left child node
        self.inorder(root.left)
        # Append current node value to output list
        self.output.append(root.val)
        # Call function on right child node
        self.inorder(root.right)
