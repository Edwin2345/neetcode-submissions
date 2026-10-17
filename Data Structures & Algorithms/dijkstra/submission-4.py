class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #build adj list
        adj, dists, paths = {}, {}, {}
        for i in range(n):
            adj[i] = []
            dists[i] = -1
            paths[i] = []
        for u,v,w in edges:
            adj[u].append( (w,v) )
        
        #add startign node to heap (dist 0, no path to it)
        minHeap = []
        heapq.heappush(minHeap, (0, src, [src]))

        #run dijstra while heap full and all other ndoes not reached
        foundNodes = 0
        while len(minHeap) > 0 and foundNodes < n:
            #pop from heap and check not vertex visited
            w1, v1, path = heapq.heappop(minHeap)
            if dists[v1] != -1:
               continue

            #mark unexplored vertex as visted and record dist/path
            dists[v1] = w1
            paths[v1] = path
            foundNodes += 1

            #add edges to heap to unexplored node
            for w2, v2 in adj[v1]:
                if dists[v2] == -1:
                   heapq.heappush(
                     minHeap,
                     (w1 + w2, v2, path + [v2])
                   ) 

        print(paths)
        return dists
