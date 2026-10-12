# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root is None:
           return levels

        q = deque([root])
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                n = q.popleft()
                level.append(n.val)
                
                if n.left:
                   q.append(n.left)
                if n.right:
                   q.append(n.right) 
            
            levels.append(list(level))
                 

        return levels