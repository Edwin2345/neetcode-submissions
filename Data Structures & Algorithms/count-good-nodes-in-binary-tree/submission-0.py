# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, maxVal, goodCnt):
        if not root:
            return None
        
        if root.val >= maxVal:
           goodCnt[0] += 1   
           maxVal = root.val 
        
        self.dfs(root.left, maxVal, goodCnt)
        self.dfs(root.right, maxVal, goodCnt)

        return goodCnt[0]
             
    def goodNodes(self, root: TreeNode) -> int:
        '''
        dfs preorder, keep maxVal during each recursive call
        maxVal is set from parent node
        '''
        return self.dfs(root, root.val, [0])

       
