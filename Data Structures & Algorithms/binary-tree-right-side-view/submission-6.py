# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #base case, empty tree
        if root is None:
           return []

        rightSide = []
        queue = deque([root]) 
        while queue:
              foundRightSide = False
              for _ in range(len(queue)):
                  #process node -> check if its the right side (first node of level)
                  node = queue.popleft()
                  if not foundRightSide:
                     rightSide.append(node.val)
                     foundRightSide = True
                
                #add children from right to left
                  if node.right: queue.append(node.right)
                  if node.left: queue.append(node.left)

        return rightSide