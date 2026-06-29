class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)        
        for n in nums:
            freqMap[n] += 1
        
        minHeap = []
        for n,freq in freqMap.items():
            heapq.heappush(minHeap, (freq,n))
            if len(minHeap) > k:
               heapq.heappop(minHeap)

        return [tup[1] for tup in minHeap] 
       
        
