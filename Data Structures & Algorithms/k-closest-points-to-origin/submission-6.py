class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use a max heap and slid through points, pop from heap when larger than size k
        #TC: NlogK as push,pop N points onto heap of size k
        #SC: K for the heap (extra space)
        max_heap = []
        for p in points:
            x,y = p[0], p[1]

            dist = (x**2 + y**2)**0.5
            heapq.heappush(
               max_heap,
               (dist * -1, x, y)
            )

            if len(max_heap) > k:
               heapq.heappop(max_heap) 

        #convert back into list of lists
        return [ [x,y] for _, x, y in max_heap]