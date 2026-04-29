# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #DFS POST ORDER
        stack = [root]
        visited = [False]

        while len(stack) > 0:
            curr = stack.pop()
            isVisit = visited.pop()

            if curr:
                #already visited -> SWAP
                if isVisit:
                   curr.left, curr.right = curr.right, curr.left
                else:
                    #Add the current node as visited and children
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        
        return root
