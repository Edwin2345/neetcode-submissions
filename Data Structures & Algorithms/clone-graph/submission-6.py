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
    #recusrively call dfs on enighbors, adding to neighbors of new node -> return new node
    #Time coplexity: O(V+E), space complexity = O(V)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #edge case: no node
        if not node:
           return None

        #initalize map new old pair of starting node
        oldToNew, q = {node: Node(node.val)}, deque([node])
        
        while len(q) > 0:
            n = q.popleft()
            for nei in n.neighbors:
                #create neighbor node if it doesn't exist
                if nei not in oldToNew:
                   oldToNew[nei] = Node(nei.val)
                   q.append(nei)   
                #add the new copy of neighbors         
                oldToNew[n].neighbors.append( oldToNew[nei] )
                    
        return oldToNew[node]
        