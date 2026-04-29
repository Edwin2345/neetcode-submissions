class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        value = -1
        while len(nums) >= k:
            value = heapq.heappop(nums)
        return value
       