# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, maxVal):
        if not root:
            return 0
        
        #check current node goodness + update maxVal
        currGood = 0
        if root.val >= maxVal:
           currGood += 1
           maxVal = root.val 
        
        #With updated maxVal along path -> check number of good nodes in LST + RST
        leftGood = self.dfs(root.left, maxVal)
        rightGood = self.dfs(root.right, maxVal)
        
        #combine all good nodes cnt to get total
        return currGood + leftGood + rightGood
             
    def goodNodes(self, root: TreeNode) -> int:
        '''
        dfs preorder, keep maxVal during each recursive call
        maxVal is set from parent node
        '''
        return self.dfs(root, root.val)

       
