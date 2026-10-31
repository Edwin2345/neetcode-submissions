# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root, subRoot):
        #compare current nodes
        if root is None and subRoot is None:
           return True
        if root is None or subRoot is None:
           return False
        if root.val != subRoot.val:
           return False 

        #check LST and RST
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case
        if root is None and subRoot is None:
           return True
        if root is None or subRoot is None:
           return False
            
        #found subtree
        if self.sameTree(root, subRoot):
           return True

        #otherwise, check other branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 