# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, p, q):
        qQueue, pQueue = deque([q]), deque([p])

        while qQueue or pQueue:
            pNode, qNode = qQueue.popleft(), pQueue.popleft()
            if pNode is None and qNode is None:
               continue
            if pNode is None or qNode is None:
               return False
            if pNode.val != qNode.val:
               return False

            qQueue.append( qNode.left )  
            qQueue.append( qNode.right ) 
            pQueue.append( pNode.left )
            pQueue.append( pNode.right ) 

        return True 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case: if root is none and subRoot not
        if root is None and subRoot is not None:
            return False
        #same tree from this node
        if self.sameTree(root, subRoot):
           return True

        #otehrwise, check if subtree is possible form left and right side
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )