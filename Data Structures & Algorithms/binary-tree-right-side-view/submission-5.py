# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        #bfs to find right side    
        queue = deque()
        queue.append(root)
        rightSide = []
        while queue:
            foundFirstRight = False
            #iterate level by level
            for i in range(len(queue)):
                cur = queue.popleft()
                if not foundFirstRight:
                    rightSide.append(cur.val)
                    foundFirstRight = True
                
                #add children -> right to left
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)

        return rightSide