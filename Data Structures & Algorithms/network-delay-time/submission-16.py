class Solution:
    #k nad n are always valid
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build adj list:  adj[src] = [ (time, dst) ]
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append( (t,v) )
        
        #add starting node to min heap (at time 0)
        min_heap = [ (0,k) ]

        #run dijkstra's until heap empty or all nodes visited
        visitedNodes = set()
        minDelayTime = 0
        while len(min_heap) > 0 and len(visitedNodes) < n:
            #pop the smallest edge to an non-visited node
            time1, n1 = heapq.heappop(min_heap)
            if n1 in visitedNodes:
               continue

            #mark node as visited and add to the total time
            minDelayTime = time1
            visitedNodes.add( n1 )

            #add edges to other unexplored nodes to min_heap
            for time2, n2 in adj[n1]:
                if n2 not in visitedNodes:
                   heapq.heappush(
                     min_heap,
                     (time1 + time2, n2)
                   ) 

        #couldnt reach all nodes
        if len(visitedNodes) < n:
           return -1
        
        return minDelayTime

