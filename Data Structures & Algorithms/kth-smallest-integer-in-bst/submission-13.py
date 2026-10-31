# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #in order dfs
        def dfs(node):
            #base case
            nonlocal k
            if node is None:
               return None
            
            #check left side
            leftNodeVal = dfs(node.left)
            if leftNodeVal is not None:
               return leftNodeVal
            
            #check current node
            k -= 1
            if k == 0:
               return node.val

            #check right side
            rightNodeVal = dfs(node.right)
            if rightNodeVal is not None:
               return rightNodeVal

        return dfs(root)

