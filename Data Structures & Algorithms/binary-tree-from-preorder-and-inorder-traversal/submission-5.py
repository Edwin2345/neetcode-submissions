# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #preorder gives current root node, inorder gives LST and RST where preorder value partitions
    #index of preorder value in inorder list - inStartIndex = Size of LST
    #convert inorder into value : index for easy search
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inOrderMap =  { val : ind for ind,val in enumerate(inorder) }
        
        def dfs(preStartIndex, preEndIndex, inStartIndex, inEndIndex):
            #base case -> completed subtrees
            if preStartIndex > preEndIndex or inStartIndex > inEndIndex:
               return None

            #create curr root at preorder start index
            node = TreeNode(preorder[preStartIndex])

            #search for node value in inorder to get lstSize
            lstSize = inOrderMap[node.val] - inStartIndex

            #recursively build LST and RST
            node.left = dfs(preStartIndex + 1, preStartIndex + lstSize, inStartIndex, inStartIndex + lstSize)
            node.right = dfs(preStartIndex + lstSize + 1, preEndIndex, inStartIndex + lstSize + 1, inEndIndex)
            return node
        
        return dfs(0, len(preorder)-1, 0, len(inorder))