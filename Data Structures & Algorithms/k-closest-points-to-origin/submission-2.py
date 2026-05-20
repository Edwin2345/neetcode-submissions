class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceFromOrigin(point):
            return ( (point[0])**2 + (point[1])**2 )**0.5
        
        max_heap = []
        for p in points:
            heapq.heappush( max_heap, (-1*distanceFromOrigin(p), p) )
            if len(max_heap) > k:
               heapq.heappop( max_heap ) 
        
        return [point for _,point in max_heap]