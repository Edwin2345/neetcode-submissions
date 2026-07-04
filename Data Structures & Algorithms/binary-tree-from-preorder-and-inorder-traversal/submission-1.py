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
    #P: use a dfs function passing indexes for proder and inorder start and end -> return none if start inde > end index
    #P: map inorder values to indeices for easy retibal
    #P: start by building current node at pre_start
    #P: find index of that node value in order (lookup), the LST_len = index - inorder_start
    #P: build LST using preorder: pre_start+1, prestart+lst_lengh, inorder: in_start, index-1
    #P: build RST using peorrder: prestart+lst_length+1 pre_end, inorder: index+1, in_end
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder or not inorder:
           return None
        
        #create a map to lookup index of value in inorder
        inorder_map  = { val : i for i,val in enumerate(inorder)}

        def dfs(pre_start_index, pre_end_index, in_start_index, in_end_index):
            #base case
            if (pre_start_index > pre_end_index) or (in_start_index > in_end_index):
               return None

            #build current node at preroder start
            node = TreeNode(preorder[pre_start_index]) 

            #look up inorder index and calc length of left  subtree
            in_index = inorder_map[node.val]
            lst_len = in_index - in_start_index

            #recuse to build LST and RST
            node.left = dfs(pre_start_index + 1, pre_start_index + lst_len, in_start_index, in_index - 1)
            node.right = dfs(pre_start_index + lst_len + 1, pre_end_index, in_index + 1, in_end_index)
             
            return node

        return dfs(0, len(preorder)-1, 0, len(inorder)-1)

     