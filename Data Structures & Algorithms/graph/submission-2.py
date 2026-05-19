class Graph:

    class Node:
        def __init__(self, val):
            self.val = val
            self.neighbors = set()
    
    def __init__(self):
        self.nodes = {}

    def addEdge(self, src: int, dst: int) -> None:
        #add src and dst nodes if nto already in graph
        if src not in self.nodes:
           self.nodes[src] = self.Node(src)
        if dst not in self.nodes:
           self.nodes[dst] = self.Node(dst)

        #make connection between src and dst
        self.nodes[src].neighbors.add(dst)  


    def removeEdge(self, src: int, dst: int) -> bool:
        #edge case: either node does not exist
        if (src not in self.nodes) or (dst not in self.nodes):
           return False
        #edge case: actual edge not exist
        if dst not in self.nodes[src].neighbors:
           return False

        #remove the edge
        self.nodes[src].neighbors.remove(dst)
        return True  


    def hasPath(self, src: int, dst: int) -> bool:
        #dfs to find path,a s we assume both exist
        visited = set()

        def dfs(nodeNum):
            #process node -> check if dst
            visited.add(nodeNum)
            if self.nodes[nodeNum].val == dst:
               return True

            #otherwise dfs to neighbors to check there (if not already visited)
            for n in self.nodes[nodeNum].neighbors:
                if n not in visited and dfs(n):
                   return True 
                  
            #not found
            return False

        return dfs(src)


