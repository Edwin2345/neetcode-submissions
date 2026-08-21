"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    #note; value of node = index in node list
    #keep map of old nodes to new
    #dfs: start with current node, make copy put in map
    #recusrively call dfs on enighbors, adding to neighbors of new node
    #return new node
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #edge case: no node
        if not node:
           return None

        oldToNew = {}
        def dfs(n):
            #already created node
            if n in oldToNew:
               return oldToNew[n]

            #else, create a copy and palce in map
            oldToNew[n] = Node(n.val)  

            #recusively make copies of its neighbors and add to new node neighbor list
            for neighbor in n.neighbors:
                oldToNew[n].neighbors.append( dfs(neighbor) )
            
            return oldToNew[n]
        
        return dfs(node)
        