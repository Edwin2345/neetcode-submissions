# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        goodCount = 0
        q = deque([ (root, float("-inf")) ])

        while len(q) > 0:
            #pop and check if current node is good
            node, maxValAbove = q.popleft()
            if node.val >= maxValAbove:
               goodCount += 1
               maxValAbove = node.val

            #add children to process
            if node.left:
               q.append( (node.left, maxValAbove) )  
            if node.right:
               q.append( (node.right, maxValAbove) ) 

        return goodCount
    