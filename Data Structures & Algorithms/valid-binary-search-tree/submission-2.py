# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #N: we are given a binary tree
    #P: do bfs but add  tuple (node, lower, upper)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        q = deque()
        if root:
           q.append( (root, float("-inf"), float("inf")) )
        
        while len(q):
            #process current
            node, low, high = q.popleft()
            if node.val <= low or node.val >= high:
               return False

            #add children
            if node.left:
               q.append( (node.left, low, node.val) )
            if node.right:
               q.append( (node.right, node.val, high) )   

        return True 
            
