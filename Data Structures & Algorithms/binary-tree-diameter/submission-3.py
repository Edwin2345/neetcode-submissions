# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, diameter):
        if not node:
           return 0
        
        #calculate diameter of current and see if its larger
        leftDepth = self.dfs(node.left, diameter)
        rightDepth =  self.dfs(node.right, diameter)
        curDiameter = leftDepth + rightDepth

        diameter[0] = max(diameter[0], curDiameter)
         
        #return depth 
        return 1 + max(leftDepth, rightDepth)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.dfs(root, diameter)
        return diameter[0]