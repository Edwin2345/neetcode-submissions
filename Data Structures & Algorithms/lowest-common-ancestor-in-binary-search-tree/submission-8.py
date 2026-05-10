# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #found a match for LCA -> is inbetween 2 values
        if (p.val <= root.val and root.val <= q.val) or (q.val <= root.val and root.val <= p.val):
           return root 
        
        #current node too large -. search left
        if root.val > max(p.val, q.val):
           return self.lowestCommonAncestor(root.left, p, q)

        #otherwsire, current node is too small -> search right
        return self.lowestCommonAncestor(root.right, p, q)