# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #convert inorder into (value, index) map for O(1) lookup
        inOrderMap = {val : index for index,val in enumerate(inorder)}

        def dfs(preStartIndex, preEndIndex, inStartIndex, inEndIndex):
            #base case
            if preStartIndex > preEndIndex or inStartIndex > inEndIndex:
               return None

            #build current node using preorder first val
            newNode = TreeNode(preorder[preStartIndex])

            #find where LST and RST partition by looking up node val in inorder
            inOrderIndex =  inOrderMap[newNode.val]
            lstSize = inOrderIndex - inStartIndex

            #build LST and RST recursively -> LST is from inStart to inOrderIndex-1, preStartIndex+1 to preStartIndex + lstSize
            newNode.left = dfs(preStartIndex + 1, preStartIndex + lstSize, inStartIndex, inOrderIndex - 1)
            newNode.right = dfs(preStartIndex + lstSize + 1, preEndIndex, inOrderIndex + 1, inEndIndex)
            return newNode
        
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)