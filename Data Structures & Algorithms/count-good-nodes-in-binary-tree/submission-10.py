# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodCount = 0
        q = deque()
        if root:
           q.append( (root, float("-inf")) )
         
        while len(q) > 0:
           node, maxPathVal = q.popleft()
           if node.val >= maxPathVal:
              goodCount += 1
              maxPathVal = node.val
           
           if node.left:
              q.append( (node.left, maxPathVal) )
           if node.right:
              q.append( (node.right, maxPathVal) ) 

        return goodCount
          