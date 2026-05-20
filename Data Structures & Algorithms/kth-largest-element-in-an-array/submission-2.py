class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #[2,3,1,5,4]
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
               heapq.heappop(min_heap)

        return min_heap[0] 