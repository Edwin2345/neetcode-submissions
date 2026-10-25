class Solution:
    #note: always given a valid value of k
    def findKthLargest(self, nums: List[int], k: int) -> int:
         
        #hepify first, then heap pop n-k times: TC --> N + (N-K)logN, SC: N (copy inital list)--> better when  k close to N
        #sliding heap of size k (push and pop when need)  TC --> NlogK, SC K --> better when k is much smaller than N
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
               heapq.heappop(min_heap)

        return min_heap[0] 


        