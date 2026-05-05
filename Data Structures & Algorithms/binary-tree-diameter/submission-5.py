# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root):
        if not root:
           return 0
        return 1 + max(self.depth(root.left), self.depth(root.right)) 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
           return 0

        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right) 
        curDiameter = leftDepth + rightDepth

        return max(curDiameter, self.diameterOfBinaryTree(root.left),  self.diameterOfBinaryTree(root.right))  
        