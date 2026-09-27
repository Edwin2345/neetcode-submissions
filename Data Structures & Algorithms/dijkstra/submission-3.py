class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #make adj list --> src : [ (weight, dst)]
        adj, shortestPathDist, shortestPath = {}, {}, {}
        for i in range(n):           
            adj[i] = []
            shortestPathDist[i] = -1
            shortestPath[i] = [] 
        for u,v,w in edges:
            adj[u].append( (v,w) )
        
        #place the starting node into the heap
        minHeap = [ (0,src,[src]) ]
        while len(minHeap) > 0:
            # pop the smallest edge from min heap
            w1, n1, path = heapq.heappop(minHeap)

            #if node already explored, pop the next edge
            if shortestPathDist[n1] != -1:
               continue
            
            #otherwise, mark down the shorest path to this node
            shortestPathDist[n1] = w1
            shortestPath[n1] = path
            
            #add edges to adjacent nodes to min heap
            for n2,w2 in adj[n1]:
                if shortestPathDist[n2] == -1:
                   heapq.heappush(
                     minHeap,
                     (w1 + w2, n2, path + [n2])
                   )
         
        print(shortestPath)
        return shortestPathDist
         
