# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        counter = k

        def dfs(node):
            nonlocal counter
            if node is None:
               return None

            n = dfs(node.left)
            if n is not None:
               return n

            counter -= 1
            if counter == 0:
               return node.val

            return dfs(node.right) 
        
        return dfs(root)

    