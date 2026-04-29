"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #empty graph
        if not node:
            return None
   
        #bfs to find solution
        queue = deque()
        queue.append(node)
        oldToNewMap = {}
        oldToNewMap[node] = Node(node.val)
     
        while queue:
            old = queue.popleft()
            for ne in old.neighbors:
                #create neibor node copy if not in map
                if ne not in oldToNewMap:
                    oldToNewMap[ne] = Node(ne.val)
                    queue.append(ne)
                #add to new node adj list
                (oldToNewMap[old]).neighbors.append(oldToNewMap[ne])
        
        #return new base node
        return oldToNewMap[node]
           

                
        
            

    