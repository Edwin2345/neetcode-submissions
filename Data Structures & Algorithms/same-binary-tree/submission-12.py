# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #add ndoes to queue, regardless if they are null    
        queue_q = deque()    
        queue_q.append(q)

        queue_p = deque()
        queue_p.append(p)

        while queue_q or queue_p:
              #process current nodes
              q = queue_q.popleft()
              p = queue_p.popleft()
              if (not p and q) or (not q and p):
                 return False
              if p and q and p.val != q.val:
                 return False
             
           #add children even if they are null
              if p:
                 queue_p.append(p.left)
                 queue_p.append(p.right)  
              if q:          
                 queue_q.append(q.left)
                 queue_q.append(q.right)
        
        return True

