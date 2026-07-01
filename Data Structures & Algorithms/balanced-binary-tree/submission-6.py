# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node):
        if not node:
           return 0
        return 1 + max(self.depth(node.left), self.depth(node.right)) 

    #O(N^2) - > find the depth of both subtrees for every node and see if
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
           return True

        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if abs(leftDepth - rightDepth) > 1:
           return False

        return self.isBalanced(root.right) and self.isBalanced(root.left)  