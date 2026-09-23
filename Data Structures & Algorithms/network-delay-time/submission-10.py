class Solution:
    #idea -> run dijstra and check all nodes reable
    #max time to reach any node is the min time for all n nodes to receive signal
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build adjacency list + shortest path dist
        shortestPathDists, adj = {}, {}
        for i in range(1,n+1):
            adj[i] = []
            shortestPathDists[i] = -1
        for u, v, t in times:
            adj[u].append( (t,v) ) 
        
        #run dijstra starting at k
        minHeap = [ (0,k) ]
        numNodesLeft, minTime = n, -1
        while len(minHeap) > 0:
              #take shortest edge 
              t1, n1 = heapq.heappop(minHeap)

              #already seen node -> pop next
              if shortestPathDists[n1] != -1:
                 continue
              
              #update is min time to reach node if not yet discoverd
              shortestPathDists[n1] = t1
              minTime = max(minTime, t1)
              numNodesLeft -= 1
              
              #add adjacent unexplored nodes to heap
              for t2,n2 in adj[n1]:
                  if shortestPathDists[n2] == -1:
                     heapq.heappush(minHeap, (t1 + t2, n2))
        
        #not possible for signal to reach all nodes
        if numNodesLeft > 0:
           return -1 
        
        return minTime
        