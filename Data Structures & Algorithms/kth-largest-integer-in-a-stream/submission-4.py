class KthLargest:
    #constructor is o(n + (n-k)log(n)) worst case
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        #turn nums into a heap of size k
        self.min_heap = list(nums)
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)  

    #add is log(k)
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
           heapq.heappop(self.min_heap) 

        return self.min_heap[0]
        
