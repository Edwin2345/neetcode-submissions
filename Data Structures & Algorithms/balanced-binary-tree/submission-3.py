# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if abs(rightDepth - leftDepth) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
