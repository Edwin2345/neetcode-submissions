# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
           return []
        
        ans = []
        return self.DFS(root,ans)
    
    def DFS(self, root, ans):
        if root is None:
           return None
        
        self.DFS(root.left, ans)
        ans.append(root.val)
        self.DFS(root.right, ans)

        return ans
