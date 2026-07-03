# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.position = k

        def dfs(node):
            if not node:
               return None

            leftVal = dfs(node.left)
            if leftVal:
               return leftVal

            self.position -= 1
            if self.position == 0:
               return node.val

            return dfs(node.right)   
        
        return dfs(root)