# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:       
        #base case
        if not root:
          return []

        levelList = []
        queue = deque([root])

        while queue:
            row = []
            for _ in range(len(queue)):
                #process current node
                cur = queue.popleft()
                row.append(cur.val)

                #add children to stack
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            #addlevelListd completed row
            levelList.append(row) 

        return levelList