class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #build adj list (undirected) -> store indiciess only to save space
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append( (dist, j) )
                adj[j].append( (dist, i) )
        

        #choose point 0 as startign poitn and add all edges to heap
        visitedIndices = set([0])
        min_heap = []
        for dist, j in adj[0]:
            heapq.heappush( min_heap, (dist, 0, j) )

        #build MST until all points visitedIndices (will always be possible)
        minConnectCost = 0
        mst = []
        while len(min_heap) > 0 and len(visitedIndices) < len(points):
            #pop smallest edge to undiscoverd node
            dist, i, j = heapq.heappop(min_heap)
            if j in visitedIndices:
               continue 

            #add undiscovered node to MST
            minConnectCost += dist
            mst.append( (points[i], points[j], dist) )
            visitedIndices.add( j )

            #add all other edges to other undiscovered nodes
            for dist, j2 in adj[j]:
                if j2 not in visitedIndices:
                   heapq.heappush(
                      min_heap,
                      (dist, j, j2)
                   ) 
        
        print(mst)
        return minConnectCost
        
