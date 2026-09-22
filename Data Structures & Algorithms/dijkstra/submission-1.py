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

           #found shortest path to unexplored node
           if shortestPathDist[n1] == -1:
              shortestPathDist[n1] = w1
              shortestPaths[n1] = path
           
           #add adjacent nodes to heap if not explored
           for w2,n2 in adj[n1]:
               if shortestPathDist[n2] == -1:
                  heapq.heappush(minHeap, 
                    (w1 + w2, n2, path + [n2])
                  )

       print(shortestPaths)
       return shortestPathDist