# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #reached leaf
        if not root:
            return None
        
        #swap child trees
        tmp = root.right
        root.right = root.left
        root.left = tmp

        #recurse to other children
        self.invertTree(root.right)
        self.invertTree(root.left)

        #return head
        return root