class Solution:
    #min_heap apporach: time O(n + klog(n)) space = O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #edge case, number of points is less than k
        if len(points) < k:
           return []

        #add a tuple containing distance to min heap --> O(n) for heapify
        min_heap = []
        for p in points:
            x, y = p[0], p[1]
            dist = (x*x + y*y)**0.5
            min_heap.append( (dist, x, y) )

        heapq.heapify(min_heap)
        
        #get k closests by poping from min heap (k smallest dist points) _. klogn
        kClosestPoints = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            kClosestPoints.append( [x,y] )

        return kClosestPoints

        