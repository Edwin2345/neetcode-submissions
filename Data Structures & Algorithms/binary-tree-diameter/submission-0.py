# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, diameter):
        if not root:
            return  0
        
        #calc longest path using LST, RST depth and save max to diamter
        leftDepth = self.dfs(root.left, diameter)
        rightDepth = self.dfs(root.right, diameter)
        diameter[0] = max(diameter[0], leftDepth + rightDepth)

        #return depth
        return 1 + max(self.dfs(root.left, diameter), self.dfs(root.right, diameter))
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        idea -> diameter = longest path of bteween two node
             -> longest path through any node is sum(LS_Height, RS_Height)
             -> find max longest path
        '''
        if not root:
            return 0

        diameter = [0]
        self.dfs(root, diameter)
        return diameter[0]
