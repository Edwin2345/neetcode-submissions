# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #clousre variable to store diameter
        diameter = 0
         
        #dfs function to compute depths of both subtree + diameter
        def dfs(r):
            nonlocal diameter

            #base case
            if not r:
               return 0
            
            #find depths of both subtrees
            leftDepth = dfs(r.left)
            rightDepth = dfs(r.right)

            #update diameter to be max val of sum of L/R depths
            diameter = max(diameter, leftDepth + rightDepth)

            #compute depths
            return 1 + max(leftDepth, rightDepth)

        dfs(root) 

        return diameter