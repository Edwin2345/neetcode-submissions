# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #diamter of binary tree is basially the max sum of the elft and right depths
    #to get depths we can do post order and return the depth upward
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter

            #base case -> empty tree has no depth
            if node is None:
               return 0

            #get depths of LST and RST
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)

            #update diameter if possible
            diameter = max(diameter, leftDepth + rightDepth)

            #return curren nodes depth
            return 1 + max(leftDepth, rightDepth)

        dfs(root)
        return diameter
        