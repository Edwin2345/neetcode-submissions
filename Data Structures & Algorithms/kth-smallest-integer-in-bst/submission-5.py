# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthValue = 0

        def dfs(node):
            nonlocal k
            nonlocal kthValue

            if node is None:
               return
            
            dfs(node.left)

            if k == 1: 
               kthValue = node.val
            k -= 1
            
            dfs(node.right)
        
        dfs(root)
        return kthValue