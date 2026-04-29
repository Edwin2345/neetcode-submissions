# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, count, kthValue):
        if not root:
           return

        #in order traversal
        self.dfs(root.left, count, kthValue)

        count[0] -= 1
        if count[0] == 0:
           kthValue[0] = root.val
           return
        
        self.dfs(root.right, count, kthValue)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthValue = [-1]
        count = [k]
        self.dfs(root, count, kthValue)

        return kthValue[0]