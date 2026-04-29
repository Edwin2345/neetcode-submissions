# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #empty tree or reached end
        if not root:
            return None

        #check if current root is a middle value between p and q
        if root.val >= min(p.val,q.val) and root.val <= max(p.val,q.val):
            return root
        
        #otherwise -> dfs to check other nodes
        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)