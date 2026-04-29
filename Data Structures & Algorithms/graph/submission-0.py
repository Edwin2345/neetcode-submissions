class Graph:
    
    def __init__(self):
        self._adjList = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self._adjList:
            self._adjList[src] = set()          
        if dst not in self._adjList:
            self._adjList[dst] = set()
        
        self._adjList[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if(
            src not in self._adjList
            or dst not in self._adjList[src] 
        ):
          return False
        
        self._adjList[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        #bfs to find path
        queue = deque()
        queue.append(src)
        visit = set()
        visit.add(src)

        while queue:
            #process cur node
            cur = queue.popleft()
            if cur == dst:
                return True
            
            #explore all neighbors
            for ne in self._adjList[cur]:
                if ne not in visit:
                    queue.append(ne)
                    visit.add(ne)

        return False

