class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #edge case: not enoguh elements to find kth larget
        if len(nums) < k:
           return []

        #use a min heap of size n and pop until k element left
        #top will be the kth largest
        min_heap = list(nums)
        heapq.heapify(min_heap)

        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return min_heap[0]