# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        ans = []

        while(len(queue) > 0):
            levelLength = len(queue)
            level = []
            #process each level
            for i in range(levelLength):
                #process node
                cur = queue.pop(0)
                level.append(cur.val)
                #append children
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            ans.append(level)
        
        return ans
