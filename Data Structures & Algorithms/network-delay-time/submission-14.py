class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build adj list
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for u,v,t in times:
            adj[u].append( (t,v) )
        
        #add starting ndoe to min heap
        minHeap = [ (0,k) ]

        #run dijstra until all nodes reached
        minDelayTime = 0
        visited = set()
        while len(minHeap) > 0 and len(visited) < n:
            #pop edge from heap and check its to an unexplored node
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visited:
               continue
            
            #update minDelayTime and makr node as visited
            minDelayTime = t1
            visited.add(v1)

            #add unepxlored nodes to minheap, keepign cumulative time (dist) to reach
            for t2, v2 in adj[v1]:
                if v2 not in visited:
                   heapq.heappush(
                     minHeap,
                     (t1 + t2, v2)
                   )  
        
        #not possible to reach all nodes
        if len(visited) != n:
           return -1
        
        return minDelayTime
            
