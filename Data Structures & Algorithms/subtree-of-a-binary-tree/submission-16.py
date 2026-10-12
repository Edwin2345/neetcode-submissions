# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, p, q):
        if p is None and q is None:
           return True
        if p is None or q is None:
           return False  
        if p.val != q.val:
           return False 
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right) 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case: if root is none and subRoot not
        if root is None and subRoot is not None:
            return False
        #same tree from this node
        if self.sameTree(root, subRoot):
           return True

        #otehrwise, check if subtree is possible form left and right side
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )