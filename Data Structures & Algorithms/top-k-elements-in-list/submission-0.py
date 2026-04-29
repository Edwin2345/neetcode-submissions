class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get frequency
        freqCnt = {}
        for n in nums:
            if n in freqCnt:
               freqCnt[n] += 1
            else:
               freqCnt[n] = 1
        print(freqCnt)
        
        #heap solution -> keep min heap of k largest (pop the smaller one oth)
        heap = []
        for n,v in freqCnt.items():
            heapq.heappush(heap, (v,n))
            if len(heap) > k:
               heapq.heappop(heap)
        print(heap)
        
        #return top k elemnts (k)
        topK = []
        for _ in range(k):
            topK.append(heapq.heappop(heap)[1])
        
        return topK
        