# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        if not root:
           return rightSide

        q = deque([root])
        while len(q) > 0:
            foundRightSide = False
            for _ in range(len(q)):
                node = q.popleft()
                if not foundRightSide:
                   rightSide.append( node.val )
                   foundRightSide = True 
                
                if node.right:
                   q.append(node.right)
                if node.left:
                   q.append(node.left) 

        return rightSide 