# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        visited = []
        cur = root 

        while cur or stack:
            #add to stack madn go left as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            #pop from stack and process
            node =  stack.pop()
            visited.append(node.val)
          
            #go to right subtree
            cur = node.right
        
        return visited