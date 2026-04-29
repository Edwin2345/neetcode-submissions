# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        cnt = [k]
        ans = [-1]
        self.dfsInorder(root,cnt, ans)
        return ans[0]
    
    def dfsInorder(self, root, cnt, ans):
        if not root:
            return None
          
        self.dfsInorder(root.left, cnt, ans)
        
        cnt[0] -= 1
        if cnt[0] == 0:
           ans[0] = root.val

        self.dfsInorder(root.right, cnt, ans) 