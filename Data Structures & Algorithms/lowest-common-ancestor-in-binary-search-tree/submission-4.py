# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #BST -> find the middle value node from the root, will be LCA 
        if root is None:
            return None
        
        cur = root
        while cur:
            #found middle node -> LCA
            if min(p.val,q.val) <= cur.val and cur.val <= max(p.val, q.val):
                return cur
            #node too small, search right subtree
            elif min(p.val,q.val) > cur.val:
                cur = cur.right
            #node to large
            else:
                cur = cur.left
        
        #must find a node if p and q are both in tree
        return None
