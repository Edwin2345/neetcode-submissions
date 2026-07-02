# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
               return (0,True)
            
            leftDepth, isLeftBal = dfs(node.left)
            rightDepth, isRightBal = dfs(node.right)
            depth = 1 + max(leftDepth, rightDepth)

            if not isLeftBal or not isRightBal:
               return (depth, False)
            if abs(leftDepth - rightDepth) > 1:
               return (depth, False)
            
            return (depth, True)

        return dfs(root)[1]    
        