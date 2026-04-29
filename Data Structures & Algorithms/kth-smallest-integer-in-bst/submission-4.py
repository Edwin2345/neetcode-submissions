# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, node: Optional[TreeNode], k: int) -> int:
        count = k
        kthValue = -1

        #inner function
        def dfs(node):
            nonlocal count
            nonlocal kthValue

            if not node:
               return

            #in order traversal
            dfs(node.left)

            count -= 1
            if count == 0:
               kthValue = node.val
               return
            
            dfs(node.right)

        dfs(root)
        return kthValue