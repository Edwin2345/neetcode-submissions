# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #convert inorder list into map to look up idnices easier
        inOrderMap = {val : index for index,val in enumerate(inorder)}

        #global variable to track preorder index
        self.preOrderIndex = 0

        def dfs(leftIndex, rightIndex):
            #Base case, children of leaves
            if leftIndex > rightIndex:
               return None
            
            #build root node from prorder list
            root = TreeNode( preorder[self.preOrderIndex] )
            self.preOrderIndex += 1

            #look up inOrder index to partition LST and RST
            inOrderIndex = inOrderMap[root.val]
            
            #recursively build children and return finished root
            root.left = dfs(leftIndex, inOrderIndex-1)
            root.right = dfs(inOrderIndex+1, rightIndex)
            return root 
        

        return dfs(0, len(preorder)-1)
             