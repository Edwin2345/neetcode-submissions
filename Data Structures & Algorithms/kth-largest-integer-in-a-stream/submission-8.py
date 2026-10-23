class KthLargest:
    # O(N + (n-k)logn)
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
       
    # O( logk )
    def add(self, val: int) -> int:
        #add to heap and if it goes over capiacty, pop smallest
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
           heapq.heappop(self.min_heap)

        #return kth largest whcih will be first value in heap array
        return self.min_heap[0] 
        
