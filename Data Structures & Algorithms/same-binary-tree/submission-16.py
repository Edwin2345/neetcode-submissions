# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue, qQueue = deque([p]), deque([q])

        while pQueue or qQueue:
            # pop current nodes and compare
            pNode = pQueue.popleft()
            qNode = qQueue.popleft()
            if pNode is None and qNode is None:
                continue
            elif pNode is None or qNode is None:
                return False
            elif pNode.val != qNode.val:
                return False

            # add children
            pQueue.append(pNode.left)
            pQueue.append(pNode.right)
            qQueue.append(qNode.left)
            qQueue.append(qNode.right)

        return True
