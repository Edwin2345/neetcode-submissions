# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#P: preorder traversal _> tiem is O(H) where h is heigth of tree, O(H) space for call stack
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root is not None:
           q.append(root)

        height = 0
        while len(q) > 0:
            height += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                   q.append(node.left)
                if node.right:
                   q.append(node.right)  
        
        return height
               