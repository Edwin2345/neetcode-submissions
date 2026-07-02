# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def preOrderDFS(node, low, high):
            if not node:
               return True
            
            if node.val <= low or node.val >= high:
               return False

            return preOrderDFS(node.left, low, node.val) \
            and preOrderDFS(node.right, node.val, high)

        return preOrderDFS(root, float("-inf"), float("inf")) 