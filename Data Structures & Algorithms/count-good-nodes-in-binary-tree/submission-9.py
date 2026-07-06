# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0

        def dfs(node, maxPathVal):
            if not node:
               return
            
            if node.val >= maxPathVal:
               self.goodCount += 1
               maxPathVal = node.val
            
            dfs(node.left, maxPathVal)
            dfs(node.right, maxPathVal)

        dfs(root, float("-inf"))
        return self.goodCount
          