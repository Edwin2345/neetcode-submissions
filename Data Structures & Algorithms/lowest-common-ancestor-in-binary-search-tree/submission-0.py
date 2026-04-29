# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchWithList(self, root, pVal, pList):
        if root is None:
            return False
        pList.append(root)
        if(root.val == pVal):
            return True
        elif(root.val > pVal):
            self.searchWithList(root.left, pVal, pList)
        else:
            self.searchWithList(root.right, pVal, pList)
    
    def searchWithSet(self, root, qVal, qSet):
        if root is None:
            return False
        qSet.add(root)
        if(root.val == qVal):
            return True
        elif(root.val > qVal):
            self.searchWithSet(root.left, qVal, qSet)
        else:
            self.searchWithSet(root.right, qVal, qSet)

 
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pList = []
        qSet = set()

        #search for p and q, building list as you go
        self.searchWithList(root, p.val, pList)
        self.searchWithSet(root, q.val, qSet)

        #iterate list in reverse order and see where they match
        for i in range(len(pList)-1, -1, -1):
            if pList[i] in qSet:
                return pList[i]
        
        return None


        