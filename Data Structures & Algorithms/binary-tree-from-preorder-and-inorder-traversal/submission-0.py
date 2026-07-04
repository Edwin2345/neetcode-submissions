# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #N: Nodes are unique
    #N: Just Binary Tree NOT BST necessarily
    #N: the preorder list is always the root, inorder tells whats on the LST and RST by the left and right partitions of the array
    #P: make the root using preorder[0]
    #P: search for root val in inorder, the index gives the lenghts of the left subtree
    #P: for LST pass preorder[1:index+1] inorder[:index]
    #P: for RST pass preorder[index+1:] inorder[index+1:]
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder or not inorder:
           return None

        #build current node using first in preoroder
        node = TreeNode(preorder[0])

        #find that node value's index in inorder to get length of left subtree
        leftSubTreeLen = -1
        for i,n in enumerate(inorder):
            if node.val == n:
               leftSubTreeLen = i
               break

        # build LST and RST using partiong
        node.left = self.buildTree( preorder[1:leftSubTreeLen+1], inorder[:leftSubTreeLen] )
        node.right = self.buildTree( preorder[leftSubTreeLen+1:], inorder[leftSubTreeLen+1:])
        return node
     