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
   #Tiem compelxity O(n), Space COmpelxity: O(h)
   def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
       #check current node is LCA (includvely in middle)
       if not root:
          return None
       if min(p.val, q.val) <= root.val <= max(p.val, q.val):
          return root
       
       #root too big -> search left
       if root.val > max(p.val, q.val):
          return self.lowestCommonAncestor(root.left, p, q)
       #root too small -> search right
       return self.lowestCommonAncestor(root.right, p, q)

