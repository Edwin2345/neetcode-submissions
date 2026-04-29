# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []
        
        if root:
          queue.append(root)

        while(len(queue) > 0):
            rowLength = len(queue)
            row = []
            
            for i in range(rowLength):
                  curr = queue.pop(0)
                  row.append(curr.val)

                  if(curr.left):
                    queue.append(curr.left)
                  if(curr.right):
                    queue.append(curr.right)
            
            ans.append(row)

        return ans