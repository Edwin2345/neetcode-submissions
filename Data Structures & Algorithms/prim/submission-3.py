class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        #build undirected adj list
        adj = {}
        for i in range(n):
            adj[i] = []
        for u,v,w in edges:
            adj[u].append( (w,v) )
            adj[v].append( (w,u) )
        
        #pick a starting node and add its edges to heap
        minHeap = []
        for w,v in adj[0]:
            heapq.heappush(
                minHeap,
                (w,0,v)
            )
        
        #run prims until all nodes visited
        visited = set([0])
        mst = []
        totalCost = 0
        while len(minHeap) > 0 and len(visited) < n:
            #pop smallest edge to an unexplored node
            w, src, dst = heapq.heappop(minHeap)
            if dst in visited:
               continue

            #add that edge to mst and mark dst as visited
            mst.append( [src, dst, w] )
            totalCost += w
            visited.add(dst)

            #add edges from dst to unexplored nodes to grow frontier
            for w2, v2 in adj[dst]:
                if v2 not in visited:
                   heapq.heappush(
                     minHeap,
                     (w2, dst, v2)
                   ) 

        #cant connect all nodes into an MST
        if len(visited) < n:
           return -1 

        print(mst)
        return totalCost