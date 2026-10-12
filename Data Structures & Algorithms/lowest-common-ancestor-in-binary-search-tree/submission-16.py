# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # lowest common ancestor is the first node that is between the 2 node values starting from root
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)
        
        while root:
            if minVal <= root.val <= maxVal:
               return root
            if root.val > maxVal:
               root = root.left
            else:
               root = root.right  
         
        return None
