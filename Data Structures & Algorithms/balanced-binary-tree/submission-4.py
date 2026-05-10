# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n^2) solution -> each nod cehck if height left == height right +/-1
class Solution:
    def depth(self, root):
        if root is None:
           return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
           return True

        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
           return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)   