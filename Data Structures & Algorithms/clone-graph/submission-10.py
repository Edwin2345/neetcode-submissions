"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #base case -> empty graph
        if not node:
           return None 
        
        #bfs
        q = deque([node])
        oldToNew = {}
        while len(q) > 0:
            #pop and make a copy of node
            n = q.popleft()
            if n not in oldToNew:
               oldToNew[n] = Node(n.val)

            #copy its neighbors
            for n1 in n.neighbors:
                #neighbor not processed -> shallow copy and add to quee (so its children can be added) 
                if n1 not in oldToNew:
                   oldToNew[n1] = Node(n1.val)
                   q.append(n1)
                oldToNew[n].neighbors.append( oldToNew[n1] )

        return oldToNew[node]