# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, diameter):
        if not root:
            return  0
        
        #calc longest path using LST, RST depth and save max to diamter
        leftDepth = self.dfs(root.left, diameter)
        rightDepth = self.dfs(root.right, diameter)
        diameter[0] = max(diameter[0], leftDepth + rightDepth)

        #return depth
        return 1 + max(leftDepth, rightDepth)
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #idea -> dfs depth, but calc\update diameter
        #     -> diameter is calc by using sum of LST depth and RST depth
      
        if not root:
            return 0

        diameter = [0]
        self.dfs(root, diameter)
        return diameter[0]
