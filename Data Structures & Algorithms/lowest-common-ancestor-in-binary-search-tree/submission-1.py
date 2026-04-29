# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getNodePath(self, root, targetNode, path):
        if not root:
            return False

        # process current node
        path.append(root) if type(path) is list else path.add(root)
        if root.val == targetNode.val:
            return True

        # check LST and RST
        foundLeft = self.getNodePath(root.left, targetNode, path)
        foundRight = self.getNodePath(root.right, targetNode, path)
        if(foundLeft or foundRight):
            return True   

        path.pop() if type(path) is list else path.remove(root)

        return False

            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #BINARY TREE SOLUTION
        #get the paths to two nodes, then traverse backwards to see when common
        pPath = []
        qSet = set()
        self.getNodePath(root, p, pPath)
        self.getNodePath(root, q, qSet)

        for i in range(len(pPath)-1,-1,-1):
            if pPath[i] in qSet:
                return pPath[i]








