# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, cur, maxNodeVal):
        goodCount = 0
        #edge case -> node is null
        if not cur:
            return goodCount

        #found a good path
        if cur.val >= maxNodeVal:
            maxNodeVal = cur.val
            goodCount += 1

        #calculate new max node and recurse to children
        goodCount += self.dfs(cur.left, maxNodeVal)
        goodCount += self.dfs(cur.right, maxNodeVal)
        
        return goodCount

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,-101)