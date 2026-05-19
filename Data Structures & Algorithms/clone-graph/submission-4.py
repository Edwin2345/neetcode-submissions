"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # idea, keep a map (val -> newNode) of created nodes
    # then we can reuse refernce when populatign adjacency list

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #base case: empty graph
        if node is None:
           return None
        
        #bfs
        newNodeMap = {}
        queue = deque()       

        #add starting node and create intial copy
        queue.append(node)
        newNodeMap[node.val] = Node(node.val)

        #iterate throguh neighbors
        # if copy exist uses
        # else, creat it, add to map, and add new neighbor queue
        while len(queue):
              for _ in range(len(queue)):                
                  node = queue.popleft()                    
                
                  for nei in node.neighbors:
                      if nei.val not in newNodeMap:
                         newNodeMap[nei.val] =  Node(nei.val)                    
                         queue.append(nei)    
                      newNodeMap[node.val].neighbors.append( newNodeMap[nei.val] )         
                         
        return newNodeMap[1]

       