class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
       #initalize adj list and dicts
       adj = {}
       shortestPathDist = {}
       shortestPaths = {}
       for i in range(n):
          adj[i] = []
          shortestPathDist[i] = -1
          shortestPaths[i] = []
        
       #put edges in adj list
       for srcNode, dstNode, weight in edges:
           adj[srcNode].append( (weight, dstNode) )
        
       minHeap = [ (0,src,[src]) ]
       while minHeap:
           #get shortest edge
           w1, n1, path = heapq.heappop(minHeap)

           #if node already visited, get next shortest
           if shortestPathDist[n1] != -1:
              continue
           
           #visit the unepxlroed ndoe and recort its path/distiance
           shortestPathDist[n1] = w1
           shortestPaths[n1] = path

           #add edges to unexplroed nodes to minHeap
           for w2,n2 in adj[n1]:
               if shortestPathDist[n2] == -1:
                  heapq.heappush( 
                     minHeap, (w1 + w2, n2, path + [n2])
                  )

       print(shortestPaths)
       return shortestPathDist