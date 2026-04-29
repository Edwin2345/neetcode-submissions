# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=1) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return depth

        return max(self.maxDepth(root.right, depth+1), self.maxDepth(root.left, depth+1))

           
       