# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.position = k

        def inOrderDFS(node):
            if not node:
               return

            foundKthVal = inOrderDFS(node.left)
            if foundKthVal is not None:
               return foundKthVal 

            self.position -= 1
            if self.position == 0:
               return node.val

            return inOrderDFS(node.right)  
                
        return inOrderDFS(root)