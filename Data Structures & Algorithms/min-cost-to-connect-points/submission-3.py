class Solution:
    #this is an mST pronblem _. want toal cost to conenct all poitns (1 path betwen every pair)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #build adj list -> but only store indices as more space/tiem effeicnt
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                w =  abs(x2 - x1) + abs(y2 - y1)

                adj[i].append( (w,j) )
                adj[j].append( (w,i) )
        
        #pick a starign point and add edges to neighbros to min heap
        #mark as visited
        minHeap = []
        for w, neighbor in adj[0]:
            heapq.heappush(minHeap, (w, 0, neighbor))
        visitedIndices = set([0])

        #build mst using bfs + minHeap
        totalCost = 0
        while len(visitedIndices) < len(points):
            #pop the smallest edge to unexplored node
            w, src, dst = heapq.heappop(minHeap)
            if dst in visitedIndices:
               continue
            
            #add the cost to visit and mark node as visited
            totalCost += w
            visitedIndices.add(dst)

            #add edges from dst to other unexplored nodes to heap
            for w,neighbor in adj[dst]:
                if neighbor not in visitedIndices:
                   heapq.heappush(minHeap, (w, dst, neighbor)) 

        return totalCost


             

        


        