class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #turn into max heap
        max_heap = [n*-1 for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
              #remove two largest stones
              s1 = heapq.heappop(max_heap)*-1
              s2 = heapq.heappop(max_heap)*-1
              
              #if there not equal, add the difference as a new stone
              if s1 < s2 or s2 < s1:
                 heapq.heappush(max_heap, (abs(s2-s1))*-1)
        
        return max_heap[0]*-1 if len(max_heap) == 1 else 0