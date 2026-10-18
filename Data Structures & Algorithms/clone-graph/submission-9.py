"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(n):
            #base cases
            if n is None:
               return None
            if n in oldToNew:
               return oldToNew[n]

            #shallow copy current node
            oldToNew[n] = Node(n.val)

            #copy its neighbors aswell
            for n1 in n.neighbors:
                oldToNew[n].neighbors.append( dfs(n1) )
            
            return oldToNew[n]
        
        return dfs(node)