# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue or q_queue:
            p = p_queue.popleft()
            q = q_queue.popleft()

            #check current nodes
            if (p and not q) or (q and not p):
               return False
            if p and q and p.val != q.val:
               return False

            #add children if applicable
            if p:
               p_queue.append(p.left)
               p_queue.append(p.right)    
            if q:
               q_queue.append(q.left)
               q_queue.append(q.right) 
     
        return True