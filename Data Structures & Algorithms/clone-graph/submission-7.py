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
            #make a shallow copy first
            oldToNew[n] = Node(n.val)

            #copy its neighbors
            for neighbor in n.neighbors:
                #neighbor isn't already created --> recurse to make it in map
                if neighbor not in oldToNew:
                   dfs(neighbor)
                #append new neighbor to new node
                oldToNew[n].neighbors.append( oldToNew[neighbor] )
                  
            return oldToNew[n]

        return dfs(node)
        
        