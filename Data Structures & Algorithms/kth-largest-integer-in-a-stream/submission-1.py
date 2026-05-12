class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        #append to nums
        self.nums.append(val)

        #iterate through nums, add to a min heap with max size of k, return the first index
        minHeap = []
        for n in self.nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > self.k:
                heapq.heappop(minHeap)

        return minHeap[0]
