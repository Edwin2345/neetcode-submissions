# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #in order dfs
        stack = []
        curNode = root

        while len(stack) > 0 or curNode is not None:
            #go as left as possible
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            
            #pop from stack and process node
            curNode = stack.pop()
            k -= 1
            if k == 0:
               return curNode.val

            #go to RST
            curNode = curNode.right 

        
        #not found
        return None

