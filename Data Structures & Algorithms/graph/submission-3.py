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
        #bfs to find path, as we assume both nodes exist
        toVisit = set()
        queue = deque()

        #add starting node
        toVisit.add(src)
        queue.append(src)

        while len(queue):
            for _ in range(len(queue)):
              #process current node
              curNodeNum = queue.popleft()
              if curNodeNum == dst:
                return True

              #add  neighbors to queue if not already visited
              for n in self.nodes[curNodeNum].neighbors:
                  if n not in toVisit:
                     queue.append(n)
                     toVisit.add(n)
            
        #not found path
        return False


