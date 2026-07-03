# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Q: null tree?. Not a possibility
#P: use preorder dfs but pass max value down (as we go from root to leaf)
#P: explore all nodes (no early return) becuase a downward child can still be good
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #global vairable for count
        goodCount = [0]

        def dfs(node, maxPathVal):
            #base case
            if not node:
               return
            
            #check if current node good
            if node.val >= maxPathVal:
               goodCount[0] += 1 

            #explore children
            maxPathVal = max(maxPathVal, node.val)
            dfs(node.left, maxPathVal) 
            dfs(node.right, maxPathVal)

        dfs(root, float("-inf"))
        return goodCount[0]

        