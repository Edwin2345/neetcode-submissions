# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #preorder gives current root node, inorder gives LST and RST
    #index of inorder node - inLeftIndex = Size of LST
    #convert inorder into value : index for easy search
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inOrderMap =  { val : ind for ind,val in enumerate(inorder) }
        
        def dfs(preStart, preEnd, inStart, inEnd):
            #base case -> completed subtrees
            if preStart > preEnd or inStart > inEnd:
               return None

            #create curr root at preorder start index
            node = TreeNode(preorder[preStart])

            #search for node value in inorder to get lstSize
            lstSize = inOrderMap[node.val] - inStart

            #recursively build LST and RST
            node.left = dfs(preStart + 1, preStart + lstSize, inStart, inStart + lstSize)
            node.right = dfs(preStart + lstSize + 1, preEnd, inStart + lstSize + 1, inEnd)
            return node
        
        return dfs(0, len(preorder)-1, 0, len(inorder))