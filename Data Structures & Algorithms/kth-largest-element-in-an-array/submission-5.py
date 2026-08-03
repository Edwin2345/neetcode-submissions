class Solution:
    #time complkiext O(nlogk)
    #Space = O(N) for heap 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #edge case: not enoguh elements to find kth larget
        if len(nums) < k:
           return []

        #push and pop to min_heap to keep it size k
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) == k+1:
                heapq.heappop(min_heap) 
         
        return min_heap[0]