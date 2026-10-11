"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    #undirected graph
    #will grpah have cycles in it? --> possibly
    #no self loops or duplicate edges
    #idea; run bfs or dfs and use and oldToNew map to assign nodes
    #empty graph --> possible
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #edge case empty map
        if node is None:
           return node

        oldToNew = {}
        def dfs(n):
            #new node already created
            if n in oldToNew:
               return oldToNew[n]

            #make a shallow copy first, the copy its neighbors
            oldToNew[n] = Node(n.val)
            for neighbor in n.neighbors:
                oldToNew[n].neighbors.append( dfs(neighbor) )

            return oldToNew[n]

        return dfs(node)
        
        