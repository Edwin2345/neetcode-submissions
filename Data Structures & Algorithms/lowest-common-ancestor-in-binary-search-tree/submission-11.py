# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Q: can we assuem p and q are actually in the tree? --> Yes
    #Q: will p and q be equal _> No
    #Q: is a node an LCA of itself -> yes
    #P: LCA is the first node when doing binary search that is inclusilbvey between the 2 nod values
    #Tiem compelxity O(h), Space COmpelxity: O(h)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      
      while root:
         #root is LCA
         if min(p.val,q.val) <= root.val <= max(p.val,q.val):
            return root
         #root is too big -> search left
         if root.val > max(p.val, q.val):
            root = root.left
         #root is too small -> search right
         if root.val < min(p.val, q.val):
            root = root.right 
              
      return None