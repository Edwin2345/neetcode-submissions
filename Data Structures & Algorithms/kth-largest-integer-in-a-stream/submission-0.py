class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        #add the new element
        heapq.heappush(self.heap,val)
        topK = heapq.nlargest(self.k,self.heap)
        return topK.pop()
        
