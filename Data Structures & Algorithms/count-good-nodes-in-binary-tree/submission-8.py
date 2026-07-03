# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Q: null tree?. Not a possibility
#P: use bfs but pass max value down (as we go from root to leaf)
#P: explore all nodes (no early return) becuase a downward child can still be good
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
           return 0

        goodCount = 0
        q = deque([ (root, float("-inf")) ])

        while len(q) > 0:
            #check if current node is good and update maxPathVal
            node, maxPathVal = q.popleft()
            if node.val >= maxPathVal:
               goodCount += 1
               maxPathVal = node.val
            
            #add children
            if node.left:
               q.append( (node.left, maxPathVal) )
            if node.right:
               q.append( (node.right, maxPathVal) )  
              
        return goodCount

        