# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #BST Solution
        #because its bst, look for node in the middle, starting from root
        if root is None:
            return None

        #found middle value -> LCA
        if min(p.val, q.val) <= root.val and root.val <= max(p.val, q.val):
            return root
        
        #otherwise, search LST/RST
        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
        