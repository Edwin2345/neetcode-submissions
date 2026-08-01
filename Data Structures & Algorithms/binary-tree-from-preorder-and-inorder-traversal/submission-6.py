# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #preorder gives value of current node, inorder gives whats on left and right subtrees
    #use a map of inorder [val : index] to look up length of LST quickyl
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inOrderMap = {val : index for index,val in enumerate(inorder)}

        def dfs(preStart, preEnd, inStart, inEnd):
            #base case, null leaf
            if preStart > preEnd or inStart > inEnd:
               return None 
            
            #create curNode at preorder Value
            curNode = TreeNode(preorder[preStart])

            #look up length of LST in inorder Map
            lstLength = inOrderMap[curNode.val] - inStart

            #recursaively build LST and RST
            curNode.left = dfs(preStart + 1, preStart + lstLength, inStart, inStart + lstLength)
            curNode.right = dfs(preStart + lstLength + 1, preEnd, inStart + lstLength + 1, inEnd)

            return curNode



        return dfs(0, len(preorder)-1, 0, len(inorder))
        