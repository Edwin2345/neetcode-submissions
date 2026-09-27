class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # build adj list -> undirected
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # add any first point and its neighbors to minHeap
        # mark first point as visited
        visit = set([0])
        minHeap = []
        for neigh, w in adj[0]:
            heapq.heappush(minHeap, (w, 0, neigh))

        # run a bfs with minHeap until all nodes visited
        mst = []
        totalConnectCost = 0
        while len(visit) < n and len(minHeap) > 0:
            # pop smallest edge from heap to expand frontiner
            w, src, dst = heapq.heappop(minHeap)
            if dst in visit:
                continue

            # add the edge connecting to unexplored node to MST
            totalConnectCost += w
            mst.append([src, dst, w])
            visit.add(dst)

            # add edges from dst to other unexplored nodes to min heap
            for neigh, w in adj[dst]:
                if neigh in visit:
                    continue
                heapq.heappush(minHeap, (w, dst, neigh))

        # could not build mst --> not all nndoes conneced
        if len(visit) < n:
            return -1

        print(mst)
        return totalConnectCost
