# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
           return root
        
        queue = [root]
        while len(queue) > 0:
            levelLen = len(queue)
            for i in range(levelLen):
                curNode = queue.pop(0)
                #swap LST and RST
                curNode.left, curNode.right = curNode.right, curNode.left
                #add children
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)

        return root