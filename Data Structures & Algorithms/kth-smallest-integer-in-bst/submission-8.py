# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or len(stack) > 0:
            #go as far left as possible (AOC) and save every node
            while curr:
                stack.append(curr)
                curr = curr.left
                
            #pop from stack and process current node
            curr = stack.pop()
            k -= 1
            if k == 0:
               return curr.val
              
            #go to the right          
            curr = curr.right
        
        return -1
                    