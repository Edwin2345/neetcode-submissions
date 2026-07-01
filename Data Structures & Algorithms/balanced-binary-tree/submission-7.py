# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #O(N) - post order to find depth, and return upwards
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isTreeBalanced = True

        def dfs(node):
          if not node:
            return 0
          
          leftDepth = dfs(node.left)
          rightDepth = dfs(node.right)
          if abs(leftDepth - rightDepth) > 1:
             self.isTreeBalanced = False

          return 1 + max(leftDepth, rightDepth) 
        
        dfs(root)
        return self.isTreeBalanced
            