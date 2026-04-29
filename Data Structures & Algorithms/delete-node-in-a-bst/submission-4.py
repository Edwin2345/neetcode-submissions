# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        #search until node found
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            #target node has 0 child -> replace with null
            if not root.left and not root.right:
                return None
            #target node has 1 child -. replace with not null
            elif not root.right:
                return root.left
            elif not root.left:
                return root.right 
            # 2 children -> replace with smallest larger node value
            #            -> delete smallest larger   node        
            else:
                tmp = root.right
                while(tmp.left):
                    tmp = tmp.left
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
               
        return root