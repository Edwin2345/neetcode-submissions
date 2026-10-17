class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #create undeirected adj list of edges between every 2 points
        #use indices to track points
        adj = { i : [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append( (dist,j) )
                adj[j].append( (dist,i) )
        
        #add edges from point 0 to minHeap
        minHeap = []
        for dist, j in adj[0]:
            heapq.heappush(
               minHeap,
               (dist, 0, j) 
            )
        
        #run prims until all points connected
        visited = set([0])
        minCost = 0
        while len(minHeap) > 0 and len(visited) < len(points):
            #pop smallest edge that is to an unexplored node
            dist, src, dest = heapq.heappop(minHeap)
            if dest in visited:
               continue

          #add dst node to mst -> update minCost and makr visited
            minCost += dist
            visited.add( dest )

            #add edges to other unexplored nodes to heap
            for dist, dest2 in adj[dest]:
                if dest2 not in visited:
                   heapq.heappush(
                       minHeap,
                       (dist, dest, dest2)
                   ) 

        #return minCost no mater what, as always possible to connect n points
        return minCost


