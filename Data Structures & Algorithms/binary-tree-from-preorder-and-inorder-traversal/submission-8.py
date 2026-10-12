# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #preorder gives current node, inorder[1 .. node.val] is the entire left sub tree
    #use 4 indicies: preStart, preEnd, inStart, inEnd
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #map inorder from node to index to calc size of left sub tree in O(1) time
        inOrderMap = { node : index for index, node in enumerate(inorder) }

        def dfs( preStart, preEnd, inStart, inEnd ):
            #finished making the nodes
            if preStart > preEnd or inStart > inEnd:
               return None

            #create the root at preStart
            root = TreeNode( preorder[preStart] )

            #look up left sub tree size 
            lstSize = inOrderMap[root.val] - inStart

            #build left and right children
            #PreOrder: root nodes to create -->  left: (+1) to (+lstSize), right: (+lstSize + 1) to (preEnd)
            #InOrder: length of left sub tree --> left: (inStart) to +lstSize right: (+lstSize + 1) to (preEnd) 
            root.left = dfs(preStart + 1, preStart + lstSize, inStart, inStart + lstSize - 1)
            root.right = dfs(preStart + lstSize + 1, preEnd, inStart + lstSize + 1, inEnd)

            return root
        
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)




    
        