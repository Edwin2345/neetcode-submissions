# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
               return (True, 0)

            isLeftBal, leftDepth = dfs(node.left)
            isRightBal, rightDepth = dfs(node.right)

            curDepth =  1 + max(leftDepth, rightDepth)

            if not isLeftBal or not isRightBal:
               return (False, curDepth)
            if abs(leftDepth - rightDepth) > 1:
               return (False, curDepth)

            return (True, curDepth)  
        
        isTreeBal, _ = dfs(root)
        return isTreeBal
            

         