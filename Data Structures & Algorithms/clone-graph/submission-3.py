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
        
        #dfs
        newNodeMap = {}
        def dfs(n):
            #create a copy of current node
            if n.val not in newNodeMap:
               newNodeMap[n.val] = Node(n.val)

            #recurse to neighbors to make a copy of them if needed, 
            #then add to newNode adj list
            for neighbor in n.neighbors:
                #already created
                if neighbor.val in newNodeMap:
                   newNodeMap[n.val].neighbors.append( newNodeMap[neighbor.val] )
                #otherwise run dfs and then add
                else:  
                   dfs(neighbor)
                   newNodeMap[n.val].neighbors.append( newNodeMap[neighbor.val] ) 
       
        dfs(node)
        return newNodeMap[1]

       