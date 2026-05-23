# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #edge cases:
        if root is None:
           return False

        #process node, cehck if foudn valid path
        targetSum -= root.val
        if targetSum == 0 and root.left is None and root.right is None:
           return True

        #otherwsie, recurse to children
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)