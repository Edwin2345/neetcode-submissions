# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = [root]
        rsView = []

        while len(queue) > 0:
            #process rs node
            levelLength = len(queue)
            notFoundRM = True
            for i in range(levelLength):
                #pop/process node -> check if rightmost
                cur = queue.pop(0)
                if notFoundRM:
                    rsView.append(cur.val)
                    notFoundRM = False
                #append children for next level -> right first              
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        
        return rsView

                
            