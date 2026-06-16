class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create frequncy map of all cjaracters
        freqMap = {}
        for n in nums:
            if n in freqMap:
               freqMap[n] += 1
            else:
               freqMap[n] = 1


        #create tuples of num,freq and insert into min heap of size k
        minHeap = []
        for num,freq in freqMap.items():
            heapq.heappush( minHeap, (freq,num))
            if len(minHeap) > k:
               heapq.heappop(minHeap) 
        
        #return final lsit of values
        return [p[1] for p in minHeap]