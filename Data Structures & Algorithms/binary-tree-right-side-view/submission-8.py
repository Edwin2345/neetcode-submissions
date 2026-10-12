# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        if root is None:
           return rightSide

        q = deque([root])

        while len(q) > 0:
            foundRight = False
            for _ in range(len(q)):
                #pop node and add right side f nto alreayd foudn
                n = q.popleft()
                if not foundRight:
                   rightSide.append( n.val )
                   foundRight = True
                
                #add children such that right side ndoes get processed first
                if n.right:
                   q.append(n.right) 
                if n.left:
                   q.append(n.left)
        
        return rightSide
                
                
                  
        