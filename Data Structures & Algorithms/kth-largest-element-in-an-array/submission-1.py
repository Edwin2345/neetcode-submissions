class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       negnums = [-n for n in nums]
       heapq.heapify(negnums)
       for i in range(k-1):
           heapq.heappop(negnums)
       
       return -1*heapq.heappop(negnums)
       