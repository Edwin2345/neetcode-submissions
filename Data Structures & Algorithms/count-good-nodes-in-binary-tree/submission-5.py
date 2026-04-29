# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxParent=-101):
            #edge case null node
            if not node:
               return 0

            #check if curr node is greate or equal maxParent
            goodCount = 0
            if node.val >= maxParent:
               goodCount += 1    
               maxParent = node.val

            #get the good counts  
            goodCount += dfs(node.left, maxParent)
            goodCount += dfs(node.right, maxParent)

            return goodCount

        return dfs(root)