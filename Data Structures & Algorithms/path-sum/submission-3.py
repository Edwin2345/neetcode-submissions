# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, path):
            nonlocal targetSum
            # base case
            if not node:
               return None

            # process current node, check if found root to leaf path
            targetSum -= node.val
            path.append(node.val)
            if node.left is None and node.right is None and targetSum == 0:
                return path

            # otherwise, recuse to children
            leftPath = dfs(node.left, path)
            rightPath = dfs(node.right, path)
            if leftPath is not None:
                return leftPath
            if rightPath is not None:
                return rightPath

            # backtrack, remove current node from path
            path.pop()
            targetSum += node.val
            return None

        foundPath = dfs(root, [])
        print(foundPath) if foundPath else print("not found")
        return foundPath is not None
