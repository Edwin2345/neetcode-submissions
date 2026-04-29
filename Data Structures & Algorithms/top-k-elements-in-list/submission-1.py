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
        
        #heap solution -> turn freq into maxheap using heapify  O(2n) = O(n)
        heap=[]
        for n,cnt in freqCnt.items():
            heap.append((-cnt,n))
        heapq.heapify(heap)
        
        #return top k elemnts bby poping heap k times  O(klogn)
        topK = []
        for _ in range(k):
            topK.append(heapq.heappop(heap)[1])
        
        return topK
        