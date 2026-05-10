# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalTree = True

        def dfs(node):
            nonlocal isBalTree
            
            #base case -> empty tree no height
            if node is None:
               return 0

            #find hegihts of left and right subtrees
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            if abs(leftHeight - rightHeight) > 1:
               isBalTree = False

            #return new depth up to top level  
            return max(leftHeight, rightHeight) + 1
        
        dfs(root)
        return isBalTree