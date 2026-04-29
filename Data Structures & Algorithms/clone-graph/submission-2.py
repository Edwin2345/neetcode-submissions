"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #edge case -> no graph given
        if not node:
            return None
        
        #bfs to complete graph
        queue = deque()
        queue.append(node)

        #add new starting node to map
        oldToNewMap = {}
        oldToNewMap[node] = Node(node.val)

        while queue:
             old = queue.popleft()

             #add neighbors to new map
             for ne in old.neighbors:                 
                if ne not in oldToNewMap:
                    oldToNewMap[ne] = Node(ne.val)
                    queue.append(ne)
                oldToNewMap[old].neighbors.append(oldToNewMap[ne])

        #return new starting node
        return oldToNewMap[node] 
             
             
              
    
