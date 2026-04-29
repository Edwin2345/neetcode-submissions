# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #BST Solution
        if root is None:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            #check if current node is LCA
            node = queue.popleft()
            if node.val >= min(p.val,q.val) and node.val <= max(p.val,q.val):
               return node

            #otherwise, check children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        #No node found
        return None 
        