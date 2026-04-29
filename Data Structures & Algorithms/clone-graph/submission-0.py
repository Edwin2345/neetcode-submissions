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
   
        oldToNewNodeMap = {}
        def dfs(nd):
            #new node already created
            if nd in oldToNewNodeMap:
                return oldToNewNodeMap[nd]

            #create a copy of current node
            copyNode = Node(nd.val)
            oldToNewNodeMap[nd] = copyNode

            #dfs to children
            for ne in nd.neighbors:
                copyNode.neighbors.append(dfs(ne))

            return copyNode
        
        return dfs(node)