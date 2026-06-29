# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.position = k
        self.ans = None

        def inorder(node):
            if not node or self.ans is not None:
               return

            inorder(node.left)

            self.position -= 1
            if self.position == 0:
               self.ans = node.val
               return

            inorder(node.right)  
        
        inorder(root)
        return self.ans
