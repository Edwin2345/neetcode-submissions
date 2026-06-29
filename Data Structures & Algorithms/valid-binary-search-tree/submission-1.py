# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #N: we are given a binary tree
    #P: need to keep track of lower and upper bound as subtree could violate at later layer
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        def preOrderTrav(node, low, high):
            if not node:
               return True

            if node.val <= low or node.val >= high:
               return False  
            
            return preOrderTrav(node.left, low, node.val) \
            and preOrderTrav(node.right, node.val, high)
        
        return preOrderTrav(root, float("-inf"), float("inf"))
            
