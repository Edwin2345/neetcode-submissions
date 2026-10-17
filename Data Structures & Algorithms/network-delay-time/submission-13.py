class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #make adj list --> src: (time, target)
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for u,v,t in times:
            adj[u].append( (t,v) )
        
        #add starting node with weight 0
        minHeap = []
        heapq.heappush(minHeap, (0,k))
        
        #run dijstra until all ndoes visited
        minTime, visited = 0, set()
        while len(minHeap) > 0 and len(visited) < n:
            #pop smallest edge and check we didnt visit it through another path
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visited:
               continue 
            
            #mark unexplored node as visited and update network min time
            minTime = t1
            visited.add( v1 )

            #add edges to unexplored nodes to heap
            for t2, v2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush( 
                        minHeap,
                        (t1 + t2, v2)
                    ) 
        
        return minTime if len(visited) == n else -1
