# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #diametr of binary tree is argmax(depth of LST + depth of RST)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        if not root:
           return self.diameter
    
        def dfs(node):
            if not node:
               return 0

            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)

            #update diamter _. not garenteed to be rhoguh root as subtree can have greater sum
            self.diameter = max(self.diameter, leftDepth + rightDepth)

            return 1 + max(leftDepth,rightDepth)

        dfs(root)
        return self.diameter 


        