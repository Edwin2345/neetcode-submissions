# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxValAbove):
            if node is None:
               return 0
            goodCount = 0

            if node.val >= maxValAbove:
               goodCount += 1
               maxValAbove = node.val
            
            goodCount += dfs(node.left, maxValAbove)
            goodCount += dfs(node.right, maxValAbove)

            return goodCount
            
        return dfs(root, float("-inf"))
        