class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #get store the k largest nums
        self.k = k
        self.min_heap = []
        for n in nums:
            heapq.heappush(self.min_heap, n)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        #add to heap and if it goes over capiacty, pop smallest
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
           heapq.heappop(self.min_heap)

        #return kth largest whcih will be first value in heap array
        return self.min_heap[0] 
        
