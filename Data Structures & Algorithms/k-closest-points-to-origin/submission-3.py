class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
        for p in points:
            #calc distance and add to heap
            x, y = p[0], p[1]
            dist = (x**2 + y**2)**0.5
            heapq.heappush(max_heap, (dist*-1, x, y))

            #if greater than size k, remove the k+1 closest
            if len(max_heap) == k+1:
               heapq.heappop(max_heap) 
        

        #convert heap back into points
        return [ [t[1], t[2]] for t in max_heap ]

