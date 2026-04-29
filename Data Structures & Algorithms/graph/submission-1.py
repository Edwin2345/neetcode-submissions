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
        #dfs to find path
        visited = set()
        path = []
        def dfs(cur, dstn):
            #found  path
            path.append(cur)
            if cur == dstn:                
                return True
            visited.add(cur)

            
            #otherwise, check if neighbors have valid path
            for ne in self._adjList[cur]:
                if ne not in visited and dfs(ne,dstn):
                    print(path)
                    return True 
            
            #no path found  
            path.pop()    
            return False                     
                        
        return dfs(src, dst)

