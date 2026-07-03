# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] 

        while root or stack:
            #gsave cur ndoe in stack and keep going left
            while root:
               stack.append(root)
               root = root.left

            #pop from stack adn process current node
            root = stack.pop()
            k -= 1
            if k == 0:
               return root.val 

            #go right
            root = root.right 
        
        return None