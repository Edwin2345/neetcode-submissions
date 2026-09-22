class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
       #initalize shortestPath dict + adj list
       adj = {}
       shortestPath = {}
       for i in range(n):
          adj[i] = []
          shortestPath[i] = -1
        
       #put edges in adj list
       for srcNode, dstNode, weight in edges:
           adj[srcNode].append( (weight, dstNode) )
        
       minHeap = [ (0,src) ]
       while minHeap:
           #get shortest edge
           w1, n1 = heapq.heappop(minHeap)

           #mark shortest distance if node not yet explored
           if shortestPath[n1] == -1:
              shortestPath[n1] = w1
           
           #add adjacent nodes to heap if not explored
           for w2,n2 in adj[n1]:
               if shortestPath[n2] == -1:
                  heapq.heappush(minHeap, (w1 + w2, n2))
        
       return shortestPath