# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #every node must be within a max and a min (strictly < or >)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, leftMax, rightMin):
            if node is None:
               return True

            #node.val has to be in range strightly in (leftMax, rightMin)
            if node.val <= leftMax or node.val >= rightMin:
               return False

            #LST has to be less than node.val while RST has to be greater than node.val
            return (
                dfs(node.left, leftMax, node.val) and dfs(node.right, node.val, rightMin)
            )

        return dfs(root, float("-inf"), float("inf"))  
        